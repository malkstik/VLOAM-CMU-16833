# Introduction

This repository is a fork of YukunXia/VLOAM-CMU-16833, a reimplementation of the VLOAM algorithm [1], for the ROB 530 Mobile Robotics W23. Our fork replaces the FLANN kd trees in the original framework with the ikd tree[2].

The following figure [1] illustrates the pipeline of the VLOAM algorithm. 

![demo](figures/VLOAM-figure1.png)

# Results

Video: https://youtu.be/rOwxxFwpOMY

![demo](figures/evaluation.png)

The processing time for steps related to the lidar map solving (scan registration, lidar odometry, lidar mapping) is recorded to numerically compare the speed performance. With the benefit brought from ikd tree, the time in Lidar mapping process is reduced from 180.70ms to 161.72ms on average, resulting in a 10.5% improvement.  

## Prerequisites

OpenCV 4.5.1
Eigen3 3.3
Ceres 2.0
PCL 1.2

This implementation has been verified on Ubuntu 20.04.5 LTS with ROS Noetic
## Evaluation tool

The ground truth is downloaded from https://www.cvlibs.net/datasets/kitti/eval_odometry.php

The evaluation tool is from https://github.com/LeoQLi/KITTI_odometry_evaluation_tool

## Data format

Create new folder "src/vloam_main/bags/", put bags file under it.

# Reference:

[1] J. Zhang and S. Singh. Laser-visual-inertial Odometry and
Mapping with High Robustness and Low Drift. Journal of
Field Robotics. vol. 35, no. 8, pp. 1242–1264, 2018.

[2] Y. Cai, W. Xu, and F. Zhang, “ikd-tree: An incremental k-d tree for robotic applications,” 2021
