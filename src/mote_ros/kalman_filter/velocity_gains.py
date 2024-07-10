import numpy as np

class VelOptimize:
    def __init__(self, q_multiplier=1, r_multiplier=1):
        self.dt = 0.01  # Time step
        