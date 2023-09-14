# Import GPIO hardware functionality library and time-based functions
import RPi.GPIO as GPIO
import time

# Import the Motors and GUI_PI modules from the Robotics package
from Robotics import Motors
from Robotics import GUI_PI

# Define GPIO pin numbers for motors, encoders, buttons, and miniSwitches

# Define GPIO pin numbers for motor A's forward and backward movement
motorA1_forward = 2
motorA2_backward = 3

# Define GPIO pin numbers for motor B's forward and backward movement
motorB1_forward = 4
motorB2_backward = 5

# Define GPIO pin numbers for motor C's forward and backward movement
motorC1_forward =6
motorC2_backward = 7

# Define GPIO pin numbers for motor D's forward and backward movement
motorD1_forward = 8
motorD2_backward = 9

# Define GPIO pin numbers and related settings for the encoders and buttons
encoder1 = 10
lButton1 = 12
encoder1_PUD = GPIO.PUD_UP
lButton1_PUD = GPIO.PUD_DOWN
encoder1_trigg = GPIO.FALLING

# Define GPIO pin numbers and related settings for the second set of encoders and buttons.
encoder2 = 14
lButton2 = 13
encoder2_PUD = GPIO.PUD_UP
lButton2_PUD = GPIO.PUD_DOWN
encoder2_trigg = GPIO.FALLING

# Define GPIO pin numbers and related settings for the third set of mini switches, and buttons.
miniSwitch3 = 11
lButton3 = 15
miniSwitch3_PUD = GPIO.PUD_DOWN
lButton3_PUD = GPIO.PUD_DOWN
miniSwitch3_trigg = GPIO.FALLING

# Define GPIO pin numbers and related settings for the fourth set of mini switches, and buttons.
miniSwitch4 = 16
lButton4 = 17
miniSwitch4_PUD = GPIO.PUD_DOWN
lButton4_PUD = GPIO.PUD_DOWN
miniSwitch4_trigg = GPIO.FALLING

# Define GPIO pin number for the stop button
stopButton = 20

# Define functions to count rotations for all motors and stop all motors. 
# Each function takes a GPIO pin number as an argument, and increases or decreases a counter value depending on the rotation direction of the motor

# The functions are defined to count the rotations of the motors in clockwise or anti-clockwise directions. Each function takes one argument, counter_pin, 
# which represents the GPIO pin number.

def motor_rotation_count(counter_pin):

    """
    Function to count the rotation of a motor in a clockwise or anti-clockwise direction.
    
    Args:
        counter_pin (int): The GPIO pin number of the counter pin for the motor.
    """

    if motor_rotation.direction == True:
        motor_rotation.counter+=1
    else:
        motor_rotation.counter-=1

def motor_X_axis_count(counter_pin):

    """
    Function to count the rotation of the X-axis motor in a clockwise or anti-clockwise direction.
    
    Args:
        counter_pin (int): The GPIO pin number of the counter pin for the X-axis motor.
    """

    GPIO.setup(counter_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)    
    if motor_X_axis.direction == True:
        motor_X_axis.counter+=1
    else:
        motor_X_axis.counter-=1 
    
       
def motor_Y_axis_count(counter_pin):
    """
    Function to count the rotation of the Y-axis motor in a clockwise or anti-clockwise direction.
    
    Args:
        counter_pin (int): The GPIO pin number of the counter pin for the Y-axis motor.
    """

    if motor_Y_axis.direction == True:
        motor_Y_axis.counter+=1
    else:
        motor_Y_axis.counter-=1 
        
def motor_gripper_count(counter_pin):

    """
    Function to count the rotation of the gripper motor in a clockwise or anti-clockwise direction.
    
    Args:
        counter_pin (int): The GPIO pin number of the counter pin for the gripper motor.
    """
    if motor_gripper.direction == True:
        motor_gripper.counter+=1
    else:
        motor_gripper.counter-=1 
        
def motor_stop(stop_pin):

    """
    Function to stop all motors.
    
    Args:
        stop_pin (int): The GPIO pin number of the stop button.
    """

    motor_X_axis.run_robot = False
    motor_Y_axis.run_robot = False
    motor_rotation.run_robot = False
    motor_gripper.run_robot = False

# Instances are created for each motor using the DCMotor class from the Motors module
motor_rotation = Motors.DCMotor(motorA1_forward,motorA2_backward,encoder1,lButton1,encoder1_PUD, lButton1_PUD,
                                motor_rotation_count,2300,encoder1_trigg,2)
motor_Y_axis = Motors.DCMotor(motorB1_forward,motorB2_backward,encoder2,lButton2,encoder2_PUD,lButton2_PUD, 
                              motor_Y_axis_count,2200,encoder2_trigg,2)
motor_X_axis = Motors.DCMotor(motorC1_forward,motorC2_backward,miniSwitch3,lButton3,miniSwitch3_PUD,lButton3_PUD, 
                     motor_X_axis_count,75,miniSwitch3_trigg, 100)
motor_gripper = Motors.DCMotor(motorD1_forward,motorD2_backward,miniSwitch4,lButton4,miniSwitch4_PUD,lButton4_PUD, 
                      motor_gripper_count,14,miniSwitch4_trigg,80)

# Instance for controlling robot using the GUI_robot_control class from the GUI_PI module
robot_control = GUI_PI.GUI_robot_control(motor_X_axis,motor_Y_axis,motor_rotation,motor_gripper,stopButton,motor_stop)

# Execution of the robot control program
robot_control.run()



