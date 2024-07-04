#!/usr/bin/env python3

import rospy
from vectornav.msg import Ins
from geometry_msgs.msg import TwistStamped, PointStamped
from std_msgs.msg import Float32

from mote_ros.msg import State  # Replace with the actual package name if different
import numpy as np
import utm
import math
from math import sqrt
import tf.transformations
from kalman_filter import KalmanFilter
import datetime


class KalmanFilterNode:
    def __init__(self):
        self.kf = KalmanFilter()
        self.initialized = False

        self.state_pub = rospy.Publisher('kalman_state', State, queue_size=10)
        self.utm_pub = rospy.Publisher('utm_state', State, queue_size=10)
        
        rospy.Subscriber('/vectornav/INS', Ins, self.ins_callback)
        rospy.Subscriber('/vehicle/twist', TwistStamped, self.twist_callback)

        self.prev_yaw = None
        self.prev_time = None
        self.output_file_path = '/home/wizard/sharf/kalman_filter_results.txt'
        with open(self.output_file_path, 'w') as file:
            file.write('Timestamp, Q Multiplier, R Multiplier, State\n')

    def latlon_to_utm(self, lat, lon):
        utm_coords = utm.from_latlon(lat, lon)
        return utm_coords[1], utm_coords[0]  # return northing, easting

    def calculate_yaw_from_velocity(self, vel_x, vel_y):
        return math.atan2(vel_y, vel_x) * 180.0 / math.pi

    def calculate_yaw_position(self, x, y, yaw_degrees, distance=5):
        yaw_radians = math.radians(yaw_degrees)
        delta_x = distance * math.cos(yaw_radians)
        delta_y = distance * math.sin(yaw_radians)
        yaw_x = x + delta_x
        yaw_y = y + delta_y
        return yaw_x, yaw_y

    def calculate_yaw_rate(self, current_yaw_rad, current_time):
        if self.prev_yaw is not None and self.prev_time is not None:
            delta_yaw = current_yaw_rad - self.prev_yaw
            delta_time = current_time - self.prev_time
            if delta_time > 0:
                yaw_rate = delta_yaw / delta_time
            else:
                yaw_rate = 0.0
        else:
            yaw_rate = 0.0

        self.prev_yaw = current_yaw_rad
        self.prev_time = current_time
        return yaw_rate

    def publish_state(self):
        # Publish the Kalman coordinates
        state = self.kf.x
        rospy.logwarn(f"Publishing State: {state.flatten()}")
        state_msg = State()
        state_msg.x_position = state[0, 0]
        state_msg.y_position = state[1, 0]
        state_msg.velocity = state[2, 0]
        state_msg.yaw = state[3, 0]  
        state_msg.yaw_rate = state[4, 0]
        self.state_pub.publish(state_msg)

    def publish_utm(self, north, east, velocity, yaw, yawrate):
        # Publish the UTM coordinates
        utm_msg = State()
        utm_msg.x_position = north
        utm_msg.y_position = east
        utm_msg.velocity = velocity
        utm_msg.yaw = yaw
        utm_msg.yaw_rate = yawrate
        self.utm_pub.publish(utm_msg)

    def ins_callback(self, msg):
        if not self.initialized:
            north, east = self.latlon_to_utm(msg.latitude, msg.longitude)
            self.kf.x[0] = north
            self.kf.x[1] = east
            self.kf.x[2] = 0  # Initialize x-velocity assuming it starts from rest
            self.kf.x[3] = msg.yaw  # Initialize yaw
            self.initialized = True
            return

        north, east = self.latlon_to_utm(msg.latitude, msg.longitude)
        z_pos = np.array([[north], [east]])
        z_yaw = np.array([[msg.yaw]])
        z_vel = np.array([-msg.nedVelX])
        self.kf.update(z_vel, self.kf.H_vel, self.kf.R_vel)

        self.kf.predict()
        self.kf.update(z_pos, self.kf.H_pos, self.kf.R_pos)
        self.kf.update(z_yaw, self.kf.H_yaw, self.kf.R_yaw)

        self.publish_state()
        self.publish_utm(north, east, self.kf.x[2, 0], msg.yaw, self.kf.x[4, 0])
            
        self.run_iterations(north, east, self.kf.x[2, 0], msg.yaw, self.kf.x[4, 0])
        
    def twist_callback(self, msg):
        if not self.initialized:
            rospy.logwarn("Kalman filter not initialized with INS data yet")
            return  # We need INS data for proper initialization
        z_vel = np.array([[msg.twist.linear.x]])  # Assume only measure x-velocity
        z_yawrate = np.array([[msg.twist.angular.z]])

        self.kf.update(z_vel, self.kf.H_vel, self.kf.R_vel)
        self.kf.update(z_yawrate, self.kf.H_yawrate, self.kf.R_yawrate)

        # Get the current state
        north = self.kf.x[0, 0]
        east = self.kf.x[1, 0]
        yaw = self.kf.x[3, 0]

        # Calculate yaw rate from twist message
        self.publish_state()
        self.publish_utm(north, east, z_vel[0, 0], yaw, z_yawrate[0, 0])
        
        self.run_iterations(north, east, z_vel[0, 0], yaw, z_yawrate[0, 0])
    
    def run_iterations(self, north, east, vel, yaw, yawrate):
        q_multipliers = np.arange(0.1, 10.1, 0.5)
        r_multipliers = np.arange(0.1, 10.1, 0.5)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        results = []
        for q_mult in q_multipliers:
            for r_mult in r_multipliers:
                # Assuming that we need to reset the state before each prediction/update cycle
                self.kf.x = np.array([[north], [east], [vel], [yaw], [yawrate]])
                # Run a hypothetical update/predict cycle
                self.kf.Q = np.eye(5) * q_mult  # Adjust process noise
                self.kf.R_pos = np.eye(2) * r_mult  # Adjust measurement noise for position as an example

                # You might want to add self.kf.predict() and self.kf.update(...) here if applicable
                self.kf.predict()
                # Assume we're just re-using the last measurements for a hypothetical update
                self.kf.update(np.array([[north], [east]]), self.kf.H_pos, self.kf.R_pos)

                state = self.kf.x.flatten()
                result = f'{timestamp}, {q_mult}, {r_mult}, {state}\n'
                results.append(result)

        # Write the results to a text file
        with open(self.output_file_path, 'a') as file:
            file.writelines(results)


if __name__ == '__main__':
    rospy.init_node('kalman_filter_node')
    node = KalmanFilterNode()
    rospy.spin()
