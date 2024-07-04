import numpy as np

class KalmanFilter:
    def __init__(self, q_multiplier=1, r_multiplier=1):
        self.dt = 0.01  # Time step

        self.A = np.array([[1, 0, self.dt, 0, 0],  # state transition matrix
                        [0, 1, 0, self.dt, 0],
                        [0, 0, 1, 0, self.dt],
                        [0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1]])
        '''
        x-position (m)
        y-position (m)
        x-velocity (m/s)
        yaw (rad)
        yaw rate (rad/s)
        '''
        self.H_pos = np.array([[1, 0, 0, 0, 0],  # Observation matrix for position
                               [0, 1, 0, 0, 0]])
        self.H_vel = np.array([[0, 0, 1, 0, 0]])  # Observation matrix for x-velocity
        self.H_yaw = np.array([[0, 0, 0, 1, 0]])  # Observation matrix for yaw
        self.H_yawrate = np.array([[0, 0, 0, 0, 1]])

        self.Q = np.eye(5) * 1  # process noise covariance 
        self.R_pos = np.eye(2) * 0.1  # measurement noise covariance for position
        self.R_vel = np.eye(1) * 0.05  # measurement noise covariance for x-velocity
        self.R_yaw = np.eye(1) * 0.1  # measurement noise covariance for yaw
        self.R_yawrate = np.eye(1) * 0.1  # measurement noise covariance for yaw rate

        '''If Q > R, relies more on measurement'''
        self.P = np.eye(5)  # estimate error covariance
        self.x = np.zeros((5, 1))  # initial state

    def predict(self):
        self.x = np.dot(self.A, self.x)  # Predict state
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q  # Predict covariance

    def update(self, z, H, R):
        S = np.dot(H, np.dot(self.P, H.T)) + R  # Measurement prediction
        K = np.dot(np.dot(self.P, H.T), np.linalg.inv(S))  # Kalman gain
        y = z - np.dot(H, self.x)  # Measurement residual
        self.x = self.x + np.dot(K, y)  # Update state
        I = np.eye(H.shape[1])  # Identity matrix
        self.P = np.dot(I - np.dot(K, H), self.P)  # Update covariance
