import RPi.GPIO as GPIO
import time
from Robotics import Motors
from Robotics import GUI_PI


motorA1_naprijed = 2
motorA2_nazad = 3

motorB1_naprijed = 4
motorB2_nazad = 5

motorC1_naprijed =6
motorC2_nazad = 7

motorD1_naprijed = 8
motorD2_nazad = 9

encoder1 = 10
lButton1 = 12
encoder1_PUD = GPIO.PUD_UP
lButton1_PUD = GPIO.PUD_DOWN
encoder1_trigg = GPIO.FALLING

encoder2 = 14
lButton2 = 13
encoder2_PUD = GPIO.PUD_UP
lButton2_PUD = GPIO.PUD_DOWN
encoder2_trigg = GPIO.FALLING

relei3 = 11
lButton3 = 15
relei3_PUD = GPIO.PUD_DOWN
lButton3_PUD = GPIO.PUD_DOWN
relei3_trigg = GPIO.FALLING

relei4 = 16
lButton4 = 17
relei4_PUD = GPIO.PUD_DOWN
lButton4_PUD = GPIO.PUD_DOWN
relei4_trigg = GPIO.FALLING

stopButton = 20


def motor_rotation_count(counter_pin):
    if motor_rotation.direction == True:
        motor_rotation.counter+=1
    else:
        motor_rotation.counter-=1

def motor_X_axis_count(counter_pin):

    GPIO.setup(counter_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)    
    if motor_X_axis.direction == True:
        motor_X_axis.counter+=1
    else:
        motor_X_axis.counter-=1 
    
       
def motor_Y_axis_count(counter_pin):
    if motor_Y_axis.direction == True:
        motor_Y_axis.counter+=1
    else:
        motor_Y_axis.counter-=1 
        
def motor_gripper_count(counter_pin):
    if motor_gripper.direction == True:
        motor_gripper.counter+=1
    else:
        motor_gripper.counter-=1 
        
def motor_stop(stop_pin):
    motor_X_axis.run_robot = False
    motor_Y_axis.run_robot = False
    motor_rotation.run_robot = False
    motor_gripper.run_robot = False


motor_rotation = Motors.DCMotor(motorA1_naprijed,motorA2_nazad,encoder1,lButton1,encoder1_PUD, lButton1_PUD,
                                motor_rotation_count,2300,encoder1_trigg,2)
motor_Y_axis = Motors.DCMotor(motorB1_naprijed,motorB2_nazad,encoder2,lButton2,encoder2_PUD,lButton2_PUD, 
                              motor_Y_axis_count,2200,encoder2_trigg,2)
motor_X_axis = Motors.DCMotor(motorC1_naprijed,motorC2_nazad,relei3,lButton3,relei3_PUD,lButton3_PUD, 
                     motor_X_axis_count,75,relei3_trigg, 100)
motor_gripper = Motors.DCMotor(motorD1_naprijed,motorD2_nazad,relei4,lButton4,relei4_PUD,lButton4_PUD, 
                      motor_gripper_count,14,relei4_trigg,80)

robot_control = GUI_PI.GUI_robot_control(motor_X_axis,motor_Y_axis,motor_rotation,motor_gripper,stopButton,motor_stop)
robot_control.run()



