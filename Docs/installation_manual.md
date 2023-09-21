# Installation Manual

The subject of these installation instructions is a Fischertechnik robotic arm (Picture 1.), controlled via Raspberry PI 3b+ (RPI) (Picture 2.).

![Figure 1. Fischertechnik robotic arm](Assets/figure1.png)

![Figure 2. Raspberry Pi 3b+ with expansion board](Assets/figure2.png)

The robotic arm, RPI, power supplies, expansion board, and driver/H-bridge are connected according to the scheme in Figure 3. The 9V power supply is used to power the DC motors of the robotic arm through the driver/H-bridge. The control of the robotic arm is done with the RPI, through the expansion board. RPI has its own power supply of 5V. GPIO pins accept voltages of 3.3V.

![Figure 3. Connection scheme for power supply, RPI, expansion board, driver/H-bridge, and robotic arm](Assets/figure3.png)

Figure 4. shows the motors of the robotic arm with pulse counting buttons for position detection on each axis, and limit switches for positioning at the end position of each axis. Motor A and motor B have built-in incremental encoders and do not require additional pulse counters. The device is also equipped with an emergency stop button for immediate stopping of the robotic arm.

![Figure 4. Robotic arm with DC motors, pulse counting buttons, and limit switches](Assets/figure4.png)

The control of the robotic arm is done with the digital GPIO pins of RPI through the expansion board. The expansion board allows for easier wiring needed for controlling the robotic arm. Figure 5 shows the pin layout on the GPIO board, as well as the corresponding connection points on the expansion board.

![Figure 5. GPIO pin layout on RPI board with corresponding connection points on the expansion board](Assets/figure5.png)

The control of the robotic arm is done through the driver/H-bridge as follows:
- Motor A (channel A on the driver) - robot rotation
- Motor B (channel B on the driver) - vertical lifting of the robot
- Motor C (channel C on the driver) - horizontal movement
- Motor D (channel D on the driver) - gripper

Connections between the driver/H-bridge and RPI (Figure 6.):
- A1 - GPIO2 - SDA
- A2 - GPIO3 - SCL
- B1 - GPIO4
- B2 - GPIO5
- C1 - GPIO6
- C2 - GPIO7 - CE1
- D1 - GPIO8 - CE0
- D2 - GPIO9 - MISO

![Figure 6. Connection of motors and RPI to the driver/H-bridge](Assets/figure6.png)

The incremental encoders on motors A and B are connected as follows (Figure 7.):
- Software-activated internal pull-up resistors
- Green wire - 0V
- Red wire - 3.3V
- Encoder1:
  - Black wire - GPIO10 - MOSI
- Encoder2:
  - Black wire - GPIO14 - TXD

![Figure 7. Connection of incremental encoders and pulse counting buttons](Assets/figure7.png)

The pulse counting buttons and emergency stop button are connected as normally open (NO) buttons. Individual buttons are connected as follows:
- Software-activated internal pull-down resistors
- Middle contact on each button is connected to 3.3V (Figure 7.)
- Green wires are connected to GPIO pins
- Limit switch 1:
  - GPIO12 - PWM0
- Limit switch 2:
  - GPIO13 - PWM1
- miniSwitch3:
  - GPIO11 - SCLK
- Limit switch 3:
  - GPIO15 - RXD
- miniSwitch4 - Gripper:
  - GPIO16
- Limit switch 4 - Gripper:
  - GPIO17
- STOP/emergencyStopButton:
  - GPIO20(PCMDin)

GPIO pins are software-configured in BCM mode

Python package installation:
- Python 3.7.3
- PySimpleGUI 4.4.1
- RPi.GPIO 0.7.0

Running the Python application in the command window:
1. Navigate to the directory with Python scripts using the cd command
2. Run "python3 Robotics_final.py"

ToDo:
- Update the application
- Flutter application for control from mobile or tablet devices
- Better driver that allows for speed variation, i.e., PWM control
- Better positioning in predetermined coordinates, currently the error caused by inertia is compensated for in software, actual and desired position.