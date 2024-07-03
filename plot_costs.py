import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from datetime import datetime

def plot_yaw_correction_data_3d(file_path):
    # Initialize lists for storing data
    yaw_corrections = []
    costs = []
    true_yaws = []
    true_costs = []
    best_yaws = []
    best_costs = []
    timestamps = []
    true_timestamps = []


    # Read the file manually to separate regular and special entries
    with open(file_path, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            if 'True Yaw' in line:
                # Handle the special summary entry
                parts = line.split(',')
                timestamp = parts[0].split(': ')[1].strip()
                true_yaw = float(parts[1].split(': ')[1].strip())
                true_cost = float(parts[2].split(': ')[1].strip())
                best_yaw = float(parts[3].split(': ')[1].strip())
                best_cost = float(parts[4].split(': ')[1].strip())
                true_timestamps.append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))
                true_yaws.append(true_yaw)
                true_costs.append(true_cost)
                best_yaws.append(best_yaw)
                best_costs.append(best_cost)
            else:
                # Handle regular data entry
                parts = line.split(',')
                timestamp = parts[0].strip()
                yaw_correction = float(parts[1].strip())
                cost = float(parts[2].strip())
                timestamps.append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))
                yaw_corrections.append(yaw_correction)
                costs.append(cost)

    # Convert lists to numpy arrays for plotting
    timestamps = np.array(timestamps)
    yaw_corrections = np.array(yaw_corrections)
    costs = np.array(costs)
    true_timestamps = np.array(true_timestamps)
    true_yaws = np.array(true_yaws)
    true_costs = np.array(true_costs)
    best_yaws = np.array(best_yaws)
    best_costs = np.array(best_costs)

    # Plotting the data
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Surface plot for regular entries
    ax.plot_trisurf(yaw_corrections, (timestamps - timestamps.min()).astype('timedelta64[s]').astype(int), costs, cmap='viridis', alpha=0.6)

    # Scatter plot for special entries
    ax.scatter(true_yaws, (true_timestamps - timestamps.min()).astype('timedelta64[s]').astype(int), true_costs, color='purple', label='True Yaw Costs', s=6)
    ax.scatter(best_yaws, (true_timestamps - timestamps.min()).astype('timedelta64[s]').astype(int), best_costs, color='b', label='Best Yaw Costs', s=6)

    ax.set_xlabel('Yaw Correction (radians)')
    ax.set_ylabel('Time (seconds from start)')
    ax.set_zlabel('Cost')
    ax.set_title('Monte Carlo Dead Reckoning for Yaw Correction')
    ax.legend()

    plt.show()
# Example call to the function
file_path = 'monte_carlo_results.txt'
plot_yaw_correction_data_3d(file_path)


# Function to plot the data
def plot_kalman_filter_results(file_path):
    data = []
    with open(file_path, 'r') as file:

        for line in file:
            parts = line.split(', ')
            timestamp = parts[0].split(': ')[1]
            q_multiplier = float(parts[1].split(': ')[1])
            r_multiplier = float(parts[2].split(': ')[1])
            initial_state = np.array(eval(parts[3].split(': ')[1]))
            predicted_state = np.array(eval(parts[4].split(': ')[1]))
            updated_state = np.array(eval(parts[5].split(': ')[1]))
            data.append([timestamp, q_multiplier, r_multiplier, initial_state, predicted_state, updated_state])
    return pd.DataFrame(data, columns=['timestamp', 'q_multiplier', 'r_multiplier', 'initial_state', 'predicted_state', 'updated_state'])
    df = parse_log_file(file_path)

    # Convert timestamp to numerical value for plotting
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['timestamp_num'] = df['timestamp'].astype(np.int64) // 10**9

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Initial state
    ax.scatter(df['timestamp_num'], df['q_multiplier'], df['r_multiplier'], c='r', marker='o', label='Initial State')

    # Predicted state
    ax.scatter(df['timestamp_num'], df['q_multiplier'], df['r_multiplier'], c='g', marker='^', label='Predicted State')

    # Updated state
    ax.scatter(df['timestamp_num'], df['q_multiplier'], df['r_multiplier'], c='b', marker='s', label='Updated State')

    ax.set_xlabel('Time')
    ax.set_ylabel('Q Multiplier')
    ax.set_zlabel('R Multiplier')
    ax.legend()

    plt.show()


# Parse the log file
file_path = "/home/wizard/sharf/kalman_results.txt"
plot_kalman_filter_results(file_path)

