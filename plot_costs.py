import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re
import matplotlib.ticker as ticker
from matplotlib import cm, colors

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
        headers = file.readline().strip().split(', ')
        state_lines = []
        timestamp, q_multiplier, r_multiplier = None, None, None

        for line in file:
            if line.strip():
                if '[' in line:  # Start of new entry
                    if state_lines:
                        state_str = ' '.join(state_lines).replace('[', '').replace(']', '').replace('\n', ' ')
                        state_values = parse_state_values(state_str)
                        if len(state_values) == 5:
                            state = np.array(state_values)
                            data.append([timestamp, q_multiplier, r_multiplier, state])
                        state_lines = []
                    parts = line.strip().split(', ')
                    timestamp = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
                    q_multiplier = float(parts[1])
                    r_multiplier = float(parts[2])
                    state_line = parts[3].strip()
                    state_lines.append(state_line)
                else:
                    state_lines.append(line.strip())

        # Process the last collected state lines
        if state_lines:
            state_str = ' '.join(state_lines).replace('[', '').replace(']', '').replace('\n', ' ')
            state_values = parse_state_values(state_str)
            if len(state_values) == 5:
                state = np.array(state_values)
                data.append([timestamp, q_multiplier, r_multiplier, state])

    return pd.DataFrame(data, columns=['timestamp', 'q_multiplier', 'r_multiplier', 'state'])

def parse_state_values(state_str):
    return [float(val) for val in re.findall(r'[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?', state_str)]

def format_axis(ax):
    ax.ticklabel_format(style='sci', axis='z', scilimits=(0,0))
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
    ax.zaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))

# Function to plot the data
def plot_kalman_filter_results(file_path):
    df = parse_log_file(file_path)
    if df.empty:
        print("No valid data to plot.")
        return

    timestamps = df['timestamp'].apply(lambda x: x.timestamp())  # Convert datetime to timestamp
    norm = colors.Normalize(vmin=timestamps.min(), vmax=timestamps.max())
    cmap = cm.viridis

    states = np.vstack(df['state'].values)
    x, y, velocity, yaw, yaw_rate = states.T
    q_multipliers, r_multipliers = df['q_multiplier'], df['r_multiplier']

    fig = plt.figure(figsize=(20, 15))

    ax1 = fig.add_subplot(231, projection='3d')
    ax1.scatter(q_multipliers, r_multipliers, x, c=timestamps, cmap=cmap, norm=norm)
    ax1.set_xlabel('Q Multiplier')
    ax1.set_ylabel('R Multiplier')
    ax1.set_zlabel('x position')
    format_axis(ax1)

    ax2 = fig.add_subplot(232, projection='3d')
    ax2.scatter(q_multipliers, r_multipliers, y, c=timestamps, cmap=cmap, norm=norm)
    ax2.set_xlabel('Q Multiplier')
    ax2.set_ylabel('R Multiplier')
    ax2.set_zlabel('y position')
    format_axis(ax2)

    ax3 = fig.add_subplot(233, projection='3d')
    ax3.scatter(q_multipliers, r_multipliers, velocity, c=timestamps, cmap=cmap, norm=norm)
    ax3.set_xlabel('Q Multiplier')
    ax3.set_ylabel('R Multiplier')
    ax3.set_zlabel('velocity')
    format_axis(ax3)

    ax4 = fig.add_subplot(234, projection='3d')
    ax4.scatter(q_multipliers, r_multipliers, yaw, c=timestamps, cmap=cmap, norm=norm)
    ax4.set_xlabel('Q Multiplier')
    ax4.set_ylabel('R Multiplier')
    ax4.set_zlabel('yaw')
    format_axis(ax4)

    ax5 = fig.add_subplot(235, projection='3d')
    ax5.scatter(q_multipliers, r_multipliers, yaw_rate, c=timestamps, cmap=cmap, norm=norm)
    ax5.set_xlabel('Q Multiplier')
    ax5.set_ylabel('R Multiplier')
    ax5.set_zlabel('yaw rate')
    format_axis(ax5)

    plt.show()


file_path = "/home/wizard/sharf/kalman_filter_results.txt"
plot_kalman_filter_results(file_path)
