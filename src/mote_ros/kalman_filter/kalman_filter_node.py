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
import datetime

import tf.transformations
from kalman_filter import KalmanFilter

class KalmanFilterNode:
    def __init__(self):
        self.kf = KalmanFilter(1, 1)  # Initialize with default multipliers
        self.initialized = False

        self.state_pub = rospy.Publisher('kalman_state', State, queue_size=10)
        self.utm_pub = rospy.Publisher('utm_state', State, queue_size=10)
        
        rospy.Subscriber('/vectornav/INS', Ins, self.ins_callback)
        rospy.Subscriber('/vehicle/twist', TwistStamped, self.twist_callback)

        self.prev_yaw = None
        self.prev_time = None

        self.q_multipliers = [0.1, 1, 10]
        self.r_multipliers = [0.1, 1, 10]

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
        state_msg = State()
        state_msg.x_position = state[0, 0]
        state_msg.y_position = state[1, 0]
        state_msg.velocity = state[2, 0]
        state_msg.yaw = state[3, 0]  
        state_msg.yaw_rate = state[4, 0]
        self.state_pub.publish(state_msg)

    def process_kalman_filter(self, north, east, yaw, vel_x, vel_yaw=None):
        for q in self.q_multipliers:
            for r in self.r_multipliers:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                kf = KalmanFilter(q, r)
                kf.x[0] = north
                kf.x[1] = east
                kf.x[2] = vel_x
                kf.x[3] = yaw
                kf.x[4] = self.kf.x[4] if vel_yaw is None else vel_yaw  # Maintain the same initial yaw rate or update if provided
                initial_state = kf.x.copy()
                kf.predict()
                predicted_state = kf.x.copy()

                # Update with position measurement
                z_pos = np.array([[north], [east]])  # Shape (2, 1)
                kf.update(z_pos, kf.H_pos, kf.R_pos)

                # Update with yaw measurement
                z_yaw = np.array([[yaw]])  # Shape (1, 1)
                kf.update(z_yaw, kf.H_yaw, kf.R_yaw)

                # Update with velocity measurement
                z_vel = np.array([[vel_x]])  # Shape (1, 1)
                kf.update(z_vel, kf.H_vel, kf.R_vel)
                
                # Update with yaw rate measurement if available
                if vel_yaw is not None:
                    z_yawrate = np.array([[vel_yaw]])  # Shape (1, 1)
                    kf.update(z_yawrate, kf.H_yawrate, kf.R_yawrate)
                
                updated_state = kf.x.copy()
                KalmanFilter.log_kalman_filter_results(timestamp, q, r, initial_state, predicted_state, updated_state)


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
        yaw = msg.yaw
        vel_x = -msg.nedVelX  # Assuming this is the correct velocity measurement
        self.process_kalman_filter(north, east, yaw, vel_x)

    def twist_callback(self, msg):
        if not self.initialized:
            rospy.logwarn("Kalman filter not initialized with INS data yet")
            return  # We need INS data for proper initialization

        north = self.kf.x[0]
        east = self.kf.x[1]
        yaw = self.kf.x[3]
        vel_x = msg.twist.linear.x
        vel_yaw = msg.twist.angular.z
        self.process_kalman_filter(north, east, yaw, vel_x, vel_yaw)

if __name__ == '__main__':
    rospy.init_node('kalman_filter_node')
    node = KalmanFilterNode()
    rospy.spin()
