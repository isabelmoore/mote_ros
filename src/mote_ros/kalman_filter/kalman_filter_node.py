#!/usr/bin/env python3

import rospy
from vectornav.msg import Ins
from geometry_msgs.msg import TwistStamped
import numpy as np
from kalman_filter import KalmanFilter
import utm

kf = KalmanFilter()
initialized = False

def latlon_to_utm(lat, lon):
    utm_coords = utm.from_latlon(lat, lon)
    return utm_coords[1], utm_coords[0]  # return northing, easting

def ins_callback(msg):
    global initialized
    if not initialized:
        north, east = latlon_to_utm(msg.latitude, msg.longitude)
        kf.x[0] = north
        kf.x[1] = east
        kf.x[2] = 0  # Initialize x-velocity assuming it starts from rest
        kf.x[3] = msg.yaw  # Initialize yaw
        initialized = True
        return

    north, east = latlon_to_utm(msg.latitude, msg.longitude)
    z_pos = np.array([[north], [east]])
    z_yaw = np.array([[msg.yaw]])
    kf.update(z_pos, kf.H_pos, kf.R_pos)
    kf.update(z_yaw, kf.H_yaw, kf.R_yaw)

    state = kf.x

    # Publish the position using ROS
    position = TwistStamped()
    position.header.stamp = rospy.Time.now()
    position.twist.linear.x = state[0, 0]
    position.twist.linear.y = state[1, 0]
    position_pub.publish(position)

    # Publish the UTM coordinates
    utm_msg = TwistStamped()
    utm_msg.header.stamp = rospy.Time.now()
    utm_msg.twist.linear.x = north
    utm_msg.twist.linear.y = east
    utm_pub.publish(utm_msg)

def twist_callback(msg):
    global initialized
    if not initialized:
        rospy.logwarn("Kalman filter not initialized with INS data yet")
        return

    z = np.array([[msg.twist.linear.x]])  # Only x-velocity considered
    kf.update(z, kf.H_vel, kf.R_vel)

if __name__ == '__main__':
    rospy.init_node('kalman_filter_node')
    position_pub = rospy.Publisher('kalman_filtered_position', TwistStamped, queue_size=10)
    utm_pub = rospy.Publisher('utm_position', TwistStamped, queue_size=10)

    rospy.Subscriber('/vectornav/INS', Ins, ins_callback)  # Adjust message type if needed
    rospy.Subscriber('/vehicle/twist', TwistStamped, twist_callback)

    rospy.spin()