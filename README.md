# MSc Advanced Computer Science - Project
## Evolutionary Based Fault Injection for Multi-Robot Systems

[Research Paper](https://github.com/tsokkisl/Evolutionary-Based-Fault-Injection-for-Multi-Robot-Systems/blob/master/docs/evolutionary_based_fault_injection_for_multi_robot_systems.pdf)

Description
---
Implementation of my MSc Advanced Computer Science project - University of York.

Instructions
---
1. **Install ROS Noetic**  
* Follow instructions on [ROS Noetic](https://www.google.comhttp://wiki.ros.org/noetic/Installation/Ubuntu)

2. **Install RosBridge**  
```
sudo apt-get install ros-noetic-rosbridge-suite
```

3. **Run instructions**  
* Run Single-Objective evolution
```
./script.sh -so
```
* Run Multi-Objective evolution
```
./script.sh -mo ['g1', ..., 'gn'] # where `gi` is the `id` of goal `i`
```
    
