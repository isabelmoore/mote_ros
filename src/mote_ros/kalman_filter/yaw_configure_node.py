#!/usr/bin/env python3

import rospy
import numpy as np
from vectornav.msg import Ins

from std_msgs.msg import Float32
from mote_ros.msg import State, Yaw, Pos
from geometry_msgs.msg import TwistStamped, PointStamped
import math
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for matplotlib
import matplotlib.pyplot as plt
import datetime



class YawConfigureNode:
    def __init__(self):
        # Initialize ROS node
        rospy.init_node('health_monitoring_node', anonymous=True)
        
        # Subscribers
        rospy.Subscriber('/vehicle/twist', TwistStamped, self.twist_callback)
        rospy.Subscriber('/vectornav/INS', Ins, self.ins_callback)
        rospy.Subscriber('/kalman_state', State, self.kalman_state_callback)

        # Publishers
        self.utm_yaw_pub = rospy.Publisher('utm_yaw_state', Yaw, queue_size=10)        
        self.kal_yaw_pub = rospy.Publisher('kal_yaw_state', Yaw, queue_size=10) 

        self.ned_yaw_pub = rospy.Publisher('ned_yaw_state', Yaw, queue_size=10) 
        self.odom_yaw_pub = rospy.Publisher('odom_yaw_state', Yaw, queue_size=10) 

        self.eul_yaw_pub = rospy.Publisher('eul_yaw_state', Yaw, queue_size=10) 
        self.monte_yaw_pub = rospy.Publisher('monte_yaw_state', Yaw, queue_size=10)

        self.true_yaw_pub = rospy.Publisher('true_yaw_state', Yaw, queue_size=10)
        self.pos_pub = rospy.Publisher('pos_states', Pos, queue_size=10)
        
        # Initialize
        self.state_kf = np.zeros((4, 1))
        self.cov_kf = np.eye(4)
        self.cov_odom = np.diag([0.1, 0.1, 0.1, 0.1])  # Example 

        self.prev_time = rospy.Time.now()
        
        self.euler_yaw = 0.0
        self.euler_yaw_rate = 0.0
        self.prev_euler_yaw = None
        self.prev_euler_time = None

        self.ned_yaw = 0.0
        self.ned_yaw_rate = 0.0
        self.prev_ned_yaw = None
        self.prev_ned_time = None

        self.utm_yaw = 0.0
        self.utm_yaw_rate = 0.0
        self.prev_utm_yaw = None
        self.prev_utm_time = None

        self.monte_yaw = 0.0
        self.monte_yaw_rate = 0.0
        self.prev_monte_yaw = None
        self.prev_monte_time = None

        self.true_yaw = 0.0
        self.true_yaw_rate = 0.0
        self.prev_true_yaw = None
        self.prev_true_time = None

        self.previous_positions = []
        self.positions = []
        self.incorrect_yaws = []
        self.velocities = []
        self.time_stamps = []

        self.prev_x = None
        self.prev_y = None
        self.step_counter = 0.0  # Counter to keep track of steps
        self.step_counter_ins = 0.0  # Counter to keep track of steps

        self.true_yaw = 0.0
        rospy.logwarn('initial yaw')
        self.output_file_path = '/home/wizard/sharf/monte_carlo_results.txt'
        with open(self.output_file_path, 'w') as file:
            file.write('Timestamp, Yaw Correction, Cost\n')

    def calculate_yaw_position(self, x, y, yaw_rad, distance=5):
        delta_x = distance * math.cos(yaw_rad)
        delta_y = distance * math.sin(yaw_rad)
        yaw_x = x + delta_x
        yaw_y = y + delta_y
        return yaw_x, yaw_y

    def twist_callback(self, msg):
        
        current_time = rospy.Time.now()
        dt = (current_time - self.prev_time).to_sec()
        self.prev_time = current_time

        self.odom_yaw_rate = msg.twist.angular.z
        self.odom_yaw = self.odom_yaw_rate * dt

    def calculate_yaw_rate(self, current_yaw_rad, prev_yaw, current_time, prev_time):
        '''
        Tasks:
        - make sure the dt for each is the same
        - apply KF to reduce noise for monte
        '''
        if prev_yaw is not None and prev_time is not None:
            delta_yaw = current_yaw_rad - prev_yaw
            delta_time = (current_time - prev_time).to_sec()
            if delta_time > 0:
                yaw_rate = delta_yaw / delta_time
            else:
                yaw_rate = 0.0
        else:
            yaw_rate = 0.0

        return yaw_rate, current_yaw_rad, current_time

    def ins_callback(self, msg):
        # B_x_prime = msg.nedVelX * np.cos(msg.pitch) + msg.nedVelZ * np.sin(msg.pitch)
        # B_y_prime = msg.nedVelX * np.sin(msg.roll) * np.sin(msg.pitch) + msg.nedVelY * np.cos(msg.roll) - msg.nedVelZ * np.sin(msg.roll) * np.cos(msg.pitch)
        
        # B_x_prime = np.cos(msg.pitch)
        # B_y_prime = np.sin(msg.roll) * np.sin(msg.pitch)
        
        current_time = rospy.Time.now()

        current_time = rospy.Time.now()
        self.step_counter_ins += 1  

        if self.step_counter_ins % 50 == 0:  
            # self.euler_yaw = np.arctan2(B_y_prime, B_x_prime)
            # self.euler_yaw_rate, self.prev_euler_yaw, self.prev_euler_time = self.calculate_yaw_rate(self.euler_yaw, self.prev_euler_yaw, current_time, self.prev_euler_time)

            # self.ned_yaw = -math.atan2(msg.nedVelX, msg.nedVelY)
            # self.ned_yaw_rate, self.prev_ned_yaw, self.prev_ned_time = self.calculate_yaw_rate(self.ned_yaw, self.prev_ned_yaw, current_time, self.prev_ned_time)

            self.utm_yaw = math.radians(msg.yaw)
            self.utm_yaw_rate, self.prev_utm_yaw, self.prev_utm_time = self.calculate_yaw_rate(self.utm_yaw, self.prev_utm_yaw, current_time, self.prev_utm_time)

    def yaw_state_pub(self, yaw, yawrate, x, y):
        yaw_x, yaw_y = self.calculate_yaw_position(x, y, yaw)
        state_msg = Yaw()
        state_msg.yaw_rad = yaw
        state_msg.yaw_rate = yawrate
        state_msg.yaw_x_position = yaw_x
        state_msg.yaw_y_position = yaw_y
        return state_msg

    def kalman_state_callback(self, msg):
        self.state_kf = np.array([[msg.x_position], [msg.y_position], [msg.velocity], [msg.yaw], [msg.yaw_rate]])
        
        current_time = rospy.Time.now()
        dt = (current_time - self.prev_time).to_sec()
        self.prev_time = current_time

        x = self.state_kf[0, 0]
        y = self.state_kf[1, 0]

        self.step_counter += 1  

        if self.step_counter % 50 == 0:  
            if self.prev_x is not None and self.prev_y is not None:
                dx = x - self.prev_x
                dy = y - self.prev_y
                self.true_yaw = np.arctan2(dy, dx)
                
                # Normalize yaw to be between -pi and pi
                self.true_yaw = (self.true_yaw + np.pi) % (2 * np.pi) - np.pi
                current_time = rospy.Time.now()

                self.true_yaw_rate, self.prev_true_yaw, self.prev_true_time = self.calculate_yaw_rate(self.true_yaw, self.prev_true_yaw, current_time, self.prev_true_time)
                # Publish the true yaw using your existing method
                self.true_yaw_pub.publish(self.yaw_state_pub(self.true_yaw, self.true_yaw_rate, x, y))

            # Update previous position on every 10th step
            self.prev_x = x
            self.prev_y = y

            # self.eul_yaw_pub.publish( self.yaw_state_pub(self.euler_yaw, self.euler_yaw_rate, x, y))
            # self.ned_yaw_pub.publish( self.yaw_state_pub(self.ned_yaw, self.ned_yaw_rate, x, y))
            self.utm_yaw_pub.publish( self.yaw_state_pub(self.utm_yaw, self.utm_yaw_rate, x, y))
            # self.odom_yaw_pub.publish( self.yaw_state_pub(self.odom_yaw, self.odom_yaw_rate, x, y))
        
        velocity = self.state_kf[2, 0]
        incorrect_yaw = self.state_kf[3, 0]
        yawrate = self.state_kf[4, 0]
        
        self.kal_yaw_pub.publish(self.yaw_state_pub(math.radians(incorrect_yaw), yawrate, x, y))
        
        self.positions.append((x, y))
        self.incorrect_yaws.append(math.radians(incorrect_yaw))
        self.velocities.append(velocity)
        self.time_stamps.append(current_time.to_sec())

        if len(self.positions) >= 50: # perform yaw correction every 50 data points
            self.correct_yaw(x, y)

    def correct_yaw(self, x, y):
        positions = np.array(self.positions)
        incorrect_yaws = np.array(self.incorrect_yaws)
        velocities = np.array(self.velocities)

        local_positions = positions - positions[0]

        best_estimate, best_corrected_yaws = self.monte_carlo_yaw_correction(
            incorrect_yaws, velocities, local_positions
        )

        current_time = rospy.Time.now()

        self.monte_yaw = (best_corrected_yaws[-1] + np.pi) % (2 * np.pi) - np.pi
        self.monte_yaw_rate, self.prev_monte_yaw, self.prev_monte_time = self.calculate_yaw_rate(
            self.monte_yaw, self.prev_monte_yaw, current_time, self.prev_monte_time
        )
        self.monte_yaw_pub.publish(self.yaw_state_pub(self.monte_yaw, self.monte_yaw_rate, x, y))

        # Reset collected data for next correction cycle
        self.positions.clear()
        self.incorrect_yaws.clear()
        self.velocities.clear()
        self.time_stamps.clear()

    def monte_carlo_yaw_correction(self, incorrect_yaws, velocities, positions):
        yaw_corrections = np.arange(-np.pi, np.pi, 0.1)
        true_corrected_yaws = (((self.true_yaw - incorrect_yaws)+ np.pi) % (2 * np.pi) - np.pi) 

        current_time = rospy.Time.now()
        dt = (current_time - self.prev_time).to_sec()
        self.prev_time = current_time
        
        positions = positions[1:] if len(positions) > 1 else positions

        trajectories = {yaw: self.compute_trajectory(incorrect_yaws + yaw, velocities, dt)[:-1] for yaw in yaw_corrections}
        true_position = self.compute_trajectory(true_corrected_yaws, velocities, dt)[:-1] 

        if len(trajectories[next(iter(trajectories))]) > 0 and len(true_position) > 0:
            costs = {yaw: np.mean((trajectory - positions) ** 2) for yaw, trajectory in trajectories.items()}
            true_cost = np.mean((true_position - positions) ** 2)
        else:
            costs = {}
            true_cost = float('inf') # if best yaw takes the min, this is inf; if max, this is 0

        if costs:
            best_yaw_correction = min(costs, key=costs.get)
            best_yaw = (best_yaw_correction + np.pi) % (2 * np.pi) - np.pi
        else:
            best_yaw = None        
        best_cost = costs.get(best_yaw, float('inf'))
        best_corrected_yaws = incorrect_yaws + best_yaw


        pos_msg = Pos()
        pos_msg.act_x_pos = positions[:, 0]
        pos_msg.act_y_pos = positions[:, 1]

        pos_msg.true_x_pos = true_position[:, 0]
        pos_msg.true_y_pos = true_position[:, 1]

        best_trajectory = trajectories[best_yaw]
        pos_msg.traj_x_pos = best_trajectory[:, 0]
        pos_msg.traj_y_pos = best_trajectory[:, 1]
        self.pos_pub.publish(pos_msg)

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log_yaw_correction(timestamp, costs, true_cost, best_yaw, best_cost, incorrect_yaws[-1])

        return best_yaw, best_corrected_yaws

    def compute_trajectory(self, yaws, velocities, dt):
        x = np.cumsum(velocities * np.cos(yaws) * dt)
        y = np.cumsum(velocities * np.sin(yaws) * dt)
        return np.vstack((x, y)).T

    def log_yaw_correction(self, timestamp, costs, true_cost, best_yaw, best_cost, incorrect_yaw):
        with open(self.output_file_path, 'a') as file:
            for yaw, cost in costs.items():
                file.write(f'{timestamp}, {yaw}, {cost}\n')
            rospy.logwarn('logging yaw')
            file.write(f'Timestamp: {timestamp}, True Yaw: {self.true_yaw - incorrect_yaw}, True Cost: {true_cost}, Best Yaw Correction: {best_yaw}, Best Cost: {best_cost}, {self.true_yaw - incorrect_yaw - best_yaw}\n')
if __name__ == '__main__':
    try:
        node = YawConfigureNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
