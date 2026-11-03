# beagle_ObjectDetector

English | [한국어](README.ko.md)

[2023] ROS 2 package for the Beagle robot that publishes roboidai camera object-detection results to a ROS 2 topic.

## Overview

`beagle_ex` is a ROS 2 `ament_python` package. It runs the roboidai `ObjectDetector` on the USB camera stream (`roboidai.Camera('usb0')`) and publishes the list of detected labels as a `my_robot_interfaces/msg/Objectlist` message on `object_topic` every 0.5 s. Detections are also shown in a camera window.

## Repository layout

```
beagle_ex/
├── package.xml, setup.py, setup.cfg, resource/   # ROS 2 ament_python package files
├── beagle_ex/beagle.py                           # object_node: object detection + Objectlist publishing
├── beagle_ex/submodules/
│   ├── ObjectDetector.py   # standalone object-detection check without ROS
│   ├── linetrice.py        # Beagle line-following example with an IP camera (blue track)
│   ├── objectback.py       # beeps and backs up when the front lidar distance is short
│   └── imported.py         # helper used to test imports
└── test/                   # default ament tests (copyright, flake8, pep257)
```

## Requirements

Dependencies from `package.xml`:

- `rclpy`, `example_interfaces`
- `roboid`, `roboidai` (Python libraries for the Beagle robot and the AI camera)
- `my_robot_interfaces` — a separate interface package that defines the `Objectlist` message; it is not included in this repository.

## Usage

`setup.py` registers the `object_node` executable (`beagle_ex.beagle:main`).

```bash
# Put beagle_ex/ under src/ of a ROS 2 workspace, then build
colcon build --packages-select beagle_ex
source install/setup.bash

ros2 run beagle_ex object_node
```

- Node name: `object_node`; topic: `object_topic` (`my_robot_interfaces/msg/Objectlist`, field `object_list`)
- On start it downloads and loads the roboidai object-detection model.

## Status

A 2023 project; no longer maintained.

## License

MIT License — see [LICENSE](LICENSE).
