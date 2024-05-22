source /opt/ros/humble/setup.sh

colcon build

source install/setup.bash

ros2 run teleop_node teleop_node