import numpy as np

class CovarianceIntersection:
    def __init__(self, omega=0.5):
        """
        Initialize the Covariance Intersection with a weight factor.
        
        :param omega: Weight factor for Covariance Intersection (default is 0.5)
        """
        self.omega = omega
    
    def fuse(self, x1, P1, x2, P2):
        """
        Perform Covariance Intersection to fuse two state estimates and their covariances.
        
        :param x1: First state estimate (numpy array) # rad
        :param P1: Covariance of the first state estimate (numpy array) # rad/s
        :param x2: Second state estimate (numpy array) # rad
        :param P2: Covariance of the second state estimate (numpy array) # rad/s
        
        :return: Fused state estimate and its covariance (numpy arrays)
        """
        P1_inv = np.linalg.inv(P1)
        P2_inv = np.linalg.inv(P2)
        
        P_CI_inv = self.omega * P1_inv + (1 - self.omega) * P2_inv
        P_CI = np.linalg.inv(P_CI_inv)
        
        x_CI = P_CI @ (self.omega * P1_inv @ x1 + (1 - self.omega) * P2_inv @ x2)
        
        return x_CI, P_CI
