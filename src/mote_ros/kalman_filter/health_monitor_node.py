import rospy
import numpy as np
from numpy.linalg import pinv, inv
from std_msgs.msg import Float32
from mote_ros.msg import Yaw, State
import math

class KalmanFilter:
    def __init__(self):
        self.x = np.array([[0.0]])  # state estimate (2D array for single variable)
        self.P = np.array([[1.0]])  # estimate covariance (2D)
        self.Q = np.array([[0.1]])  # process noise covariance (2D)
        self.R = np.array([[1.0]])  # measurement noise covariance (2D)

    def predict(self):
        self.P += self.Q   # state prediction 

    def update(self, z):
        K = self.P / (self.P + self.R)  # kalman gain -- ensure matrix operations
        self.x = self.x + K * (z - self.x)  # update state estimate
        self.P = (1 - K) * self.P  # update covariance estimate

    def get_state(self):
        return self.x[0, 0]  # state as a scalar

    def Sinverse(self):
        return np.linalg.inv(self.P + self.R) # inverse of S for Mahalanobis distance


def covariance_intersection(self, estimates, covariances, weights):
    omega = np.zeros_like(covariances[0])
    weighted_sum = np.zeros_like(estimates[0])
    total_weight = sum(weights)
    for est, cov, weight in zip(estimates, covariances, weights):
        inv_cov = np.linalg.inv(cov)
        omega += weight * inv_cov
        weighted_sum += weight * inv_cov @ est
    fused_cov = np.linalg.inv(omega)
    fused_state = fused_cov @ weighted_sum / total_weight
    return fused_state, fused_cov

class HealthMonitorNode:
    def __init__(self):
        rospy.init_node('health_monitor_node')

        self.filters = {
            'eul': KalmanFilter(),
            'ins': KalmanFilter(),
            'monte': KalmanFilter()
        }
        
        self.threshold = 5.0  # Mahalanobis thresh
        self.health_metrics = {}

        # Subscribers
        rospy.Subscriber('/eul_yaw_state', Yaw, self.eul_callback)
        rospy.Subscriber('/ins_yaw_state', Yaw, self.ins_callback)
        rospy.Subscriber('/monte_yaw_state', Yaw, self.monte_callback)
        rospy.Subscriber('/kalman_state', State, self.kalman_state_callback)

        self.fused_yaw_pub = rospy.Publisher('/fused_yaw', Yaw, queue_size=10)

        self.fused_yaw = 0.0
        self.x = 0.0
        self.y = 0.0
    def eul_callback(self, msg):
        self.process_sensor_update('eul', msg.yaw_rad)

    def ins_callback(self, msg):
        self.process_sensor_update('ins', msg.yaw_rad)

    def monte_callback(self, msg):
        self.process_sensor_update('monte', msg.yaw_rad)

    def calculate_yaw_position(self, x, y, yaw_rad, distance=5):
        delta_x = distance * math.cos(yaw_rad)
        delta_y = distance * math.sin(yaw_rad)
        yaw_x = x + delta_x
        yaw_y = y + delta_y
        return yaw_x, yaw_y

    def yaw_state_pub(self, yaw, yawrate, x, y):
        yaw_x, yaw_y = self.calculate_yaw_position(x, y, yaw)
        state_msg = Yaw()
        state_msg.yaw_rad = yaw
        state_msg.yaw_rate = yawrate
        state_msg.yaw_x_position = yaw_x
        state_msg.yaw_y_position = yaw_y
        return state_msg

    def kalman_state_callback(self, msg):
        self.x = msg.x_position
        self.y = msg.y_position
        self.fused_yaw_pub.publish(self.yaw_state_pub(self.fused_yaw, 0, self.x, self.y))

    def health_metric(self, sensor_id, mahalanobis_dist):
        health_metric = max(0, 1 - mahalanobis_dist / self.threshold)
        self.health_metrics[sensor_id] = health_metric
        
    def process_sensor_update(self, sensor_id, measurement):
        filter = self.filters[sensor_id]
        filter.predict()
        filter.update(measurement)
        S_inv = filter.Sinverse()  # inverse of the innovation covariance matrix
        measurement = np.array([measurement])  
        state_estimate = np.array([filter.get_state()])
        residual = measurement - filter.get_state()
        mahalanobis_dist = np.sqrt(residual.T @ S_inv @ residual)  # Mahalanobis distance
        
        if mahalanobis_dist > self.threshold: # if the distance exceeds a predefined threshold
            rospy.logwarn(f"Anomaly detected in {sensor_id} with Mahalanobis distance: {mahalanobis_dist}")
        
        self.health_metric(sensor_id, mahalanobis_dist)

        if all(sensor_id in self.health_metrics for sensor_id in self.filters):  # if all sensors have updated
            estimates = [f.get_state() for f in self.filters.values()]
            covariances = [f.P for f in self.filters.values()]
            weights = [self.health_metrics[sid] for sid in self.filters]  # health metrics as weights

            # weighted covariance intersection
            fused_state, fused_cov = self.covariance_intersection(estimates, covariances, weights)
            self.fused_yaw = fused_state[0]
            rospy.loginfo(f'Fused Yaw based on sensor health: {self.fused_yaw}')

        self.fused_yaw_pub.publish(self.yaw_state_pub(self.fused_yaw, 0, self.x, self.y))


    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = HealthMonitorNode()
    node.run()
