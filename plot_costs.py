import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re
import matplotlib.ticker as ticker

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
# plot_yaw_correction_data_3d(file_path)


# Function to parse the log file
def parse_log_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        state_lines = []
        timestamp, q_multiplier, r_multiplier = None, None, None

        for line in file:
            if line.startswith('Timestamp:'):
                if state_lines:
                    # Process the collected state lines
                    state_str = ' '.join(state_lines).replace('[', '').replace(']', '').strip()
                    state_values = parse_state_values(state_str)
                    if len(state_values) == 5:
                        state = np.array(state_values)
                        data.append([timestamp, q_multiplier, r_multiplier, state])
                    else:
                        print(f"Unexpected state size: {state_values} in lines: {state_lines}")
                    state_lines = []

                parts = line.split(', ')
                timestamp = parts[0].split(': ')[1]
                q_multiplier = float(parts[1].split(': ')[1])
                r_multiplier = float(parts[2].split(': ')[1])
                state_line = parts[3].split(': ')[1]
                state_lines.append(state_line)
            else:
                state_lines.append(line.strip())

        # Process the last collected state lines
        if state_lines:
            state_str = ' '.join(state_lines).replace('[', '').replace(']', '').strip()
            state_values = parse_state_values(state_str)
            if len(state_values) == 5:
                state = np.array(state_values)
                data.append([timestamp, q_multiplier, r_multiplier, state])
            else:
                print(f"Unexpected state size: {state_values} in lines: {state_lines}")

    print(f"Parsed {len(data)} entries.")
    return pd.DataFrame(data, columns=['timestamp', 'q_multiplier', 'r_multiplier', 'state'])

def parse_state_values(state_str):
    try:
        # Use regular expressions to handle scientific notation and other formats
        state_values = re.findall(r'[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?', state_str)
        return [float(val) for val in state_values]
    except ValueError as e:
        print(f"Error parsing state values: {e}")
        return []
def format_axis(ax):
    ax.ticklabel_format(style='sci', axis='z', scilimits=(0,0))  # Use scientific notation
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
    ax.zaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))

# Function to plot the data
def plot_kalman_filter_results(file_path):
    df = parse_log_file(file_path)
    if df.empty:
        print("No valid data to plot.")
        return

    # Extract state components
    states = np.vstack(df['state'])
    x = states[:, 0]
    y = states[:, 1]
    velocity = states[:, 2]
    yaw = states[:, 3]
    yaw_rate = states[:, 4]

    q_multipliers = df['q_multiplier']
    r_multipliers = df['r_multiplier']

    fig = plt.figure(figsize=(20, 15))

    # Plot x position
    ax1 = fig.add_subplot(231, projection='3d')
    ax1.scatter(q_multipliers, r_multipliers, x, c='r', marker='o', label='x position')
    ax1.set_xlabel('Q Multiplier')
    ax1.set_ylabel('R Multiplier')
    ax1.set_zlabel('x position')
    format_axis(ax1)  # Format this axis

    ax1.legend()

    # Plot y position
    ax2 = fig.add_subplot(232, projection='3d')
    ax2.scatter(q_multipliers, r_multipliers, y, c='g', marker='^', label='y position')
    ax2.set_xlabel('Q Multiplier')
    ax2.set_ylabel('R Multiplier')
    ax2.set_zlabel('y position')
    ax2.legend()

    # Plot velocity
    ax3 = fig.add_subplot(233, projection='3d')
    ax3.scatter(q_multipliers, r_multipliers, velocity, c='b', marker='s', label='velocity')
    ax3.set_xlabel('Q Multiplier')
    ax3.set_ylabel('R Multiplier')
    ax3.set_zlabel('velocity')
    ax3.legend()

    # Plot yaw
    ax4 = fig.add_subplot(234, projection='3d')
    ax4.scatter(q_multipliers, r_multipliers, yaw, c='c', marker='p', label='yaw')
    ax4.set_xlabel('Q Multiplier')
    ax4.set_ylabel('R Multiplier')
    ax4.set_zlabel('yaw')
    ax4.legend()

    # Plot yaw rate
    ax5 = fig.add_subplot(235, projection='3d')
    ax5.scatter(q_multipliers, r_multipliers, yaw_rate, c='m', marker='*', label='yaw rate')
    ax5.set_xlabel('Q Multiplier')
    ax5.set_ylabel('R Multiplier')
    ax5.set_zlabel('yaw rate')
    ax5.legend()

    plt.show()

file_path = "/home/wizard/sharf/kalman_filter_results.txt"
plot_kalman_filter_results(file_path)

test_str = "3.23088864e+06  7.05538149e+05  3.96052247e+02  3.20723496e+02 -7.87859466e+01"
parsed_values = parse_state_values(test_str)
print(parsed_values)