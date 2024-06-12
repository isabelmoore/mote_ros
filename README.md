# mote_ros

## Introduction
`mote_ros` is designed to develop a shared common operating picture (COP) for the cooperative and autonomous execution of multi-vehicle missions, integrating both aerial vehicles (AVs) and ground vehicles (GVs). This repository focuses on creating interconnected systems that enhance air-ground cooperative autonomy through shared world models, mission definitions, and dynamic environmental awareness.

## Project Objectives

### World Model and Mission Definition
- Develop a comprehensive world model containing structural and semantic information about the environment.
- Overlay a mission definition that is intricately linked with the world model to form the foundational layer of the COP.

### Inter-Vehicle Map Information Exchange
- Implement mechanisms for ground vehicle to ground vehicle (GV-GV) data exchange to enhance map accuracy and facilitate better local and global planning strategies.

### Trajectory Estimation and Information Transfer
- Enable aerial vehicles (AVs) to communicate moving object trajectory estimation (MOTE) data to ground vehicles (GVs).
- Allow GVs to dynamically replan their routes based on real-time data about obstacles, objects of interest, and potential threats from non-fleet entities.

## Installation

```bash
# Clone the repository
git clone git@github.com:isabelmoore/mote_ros.git
# Navigate to the project directory
cd mote_ros
# [Add additional setup/installation commands here]
