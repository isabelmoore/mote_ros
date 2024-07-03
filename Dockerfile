# Use the official ROS base image
FROM ros:noetic-ros-base

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    ros-noetic-rviz \
    && rm -rf /var/lib/apt/lists/*

# Setup environment variables
ENV ROS_WS=/opt/ros_ws
RUN echo "export PS1='root@mote_ros:\w\$ '" >> /root/.bashrc
# Create a workspace
RUN mkdir -p $ROS_WS/src
WORKDIR $ROS_WS

# Clone your ROS package(s) into the workspace
# Note: Replace the URL below with the actual URL or path to your ROS package(s)
# RUN git clone https://github.com/example/my_ros_package.git src/my_ros_package

# Install dependencies
RUN apt-get update && \
    rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y \
    && rm -rf /var/lib/apt/lists/*

# Build the workspace
RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; cd $ROS_WS; catkin_make'

# Source the workspace
RUN echo "source $ROS_WS/devel/setup.bash" >> ~/.bashrc

CMD ["bash"]

# Default command to run when starting the container
CMD ["roslaunch", "mote_ros", "run_both_nodes.launch"]
