# ROS 2 Battery Target Validation

## Project 7 – E-Waste Battery Extraction System

This ROS 2 package provides an initial target-pose validation
layer between the Computer Vision and Robotics components of the
E-Waste Battery Extraction project.

## Purpose

The Computer Vision pipeline will eventually provide a detected
battery target pose.

Before that target is passed into reachability checking or
MoveIt 2 motion planning, the target should be validated.

The validator currently checks:

- Coordinate frame
- X position
- Y position
- Z position
- Numerical validity
- Configured workspace boundaries

## Architecture

```text
Synthetic / CV Target
        |
        v
geometry_msgs/PoseStamped
        |
        v
/battery_target
        |
        v
Target Validator
        |
        +---- Frame validation
        |
        +---- Numerical validation
        |
        +---- Workspace validation
        |
        v
VALID / REJECTED