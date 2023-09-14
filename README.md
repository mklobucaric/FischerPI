# Robotic Arm Control GUI with Raspberry Pi 3

This Python code generates a Graphical User Interface (GUI) for controlling a robotic arm using a Raspberry Pi 3. The GUI allows users to interact with the robotic arm and perform various movements and actions.

## Installation Instructions

For detailed installation instructions and setup diagrams, please refer to the [Installation Manual](docs/installation_manual.md) and [User Guide](docs/user_guide.md).

## Features

- GUI interface for controlling the robotic arm
- Positioning and saving coordinates for the robotic arm
- Sequential execution of robotic arm commands
- Ability to save and load instructions for the robotic arm
- Homing function to return the robotic arm to its default position
- Gripper control for opening and closing

## Dependencies

- Python 3.7.3
- PySimpleGUI 4.4.1
- RPi.GPIO 0.7.0

## Usage

1. Install the required dependencies mentioned above.
2. Clone the repository to your Raspberry Pi.
3. Open a terminal and navigate to the directory with the Python scripts using the `cd` command.
4. Run the command `python3 Robotics_final.py` to launch the Python application.

## To Do

- Update the application to improve functionality and performance.
- Develop a Flutter application for control from mobile or tablet devices.
- Create a better driver that allows for speed variation and PWM control.
- Enhance positioning capabilities for more accurate movement.

For more details and information, please refer to the [User Guide](docs/user_guide.md).

![Robotic Arm GUI Screenshot](screenshots/robotic_arm_gui.png)
