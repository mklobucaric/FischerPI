import RPi.GPIO as GPIO
import time
class DCMotor():

    """
    Class for controlling a DC motor.
    """

    def __init__(self,forward_pin,back_pin,counter_pin,lButton_pin,counter_PUD,lButton_PUD,callback_name,
                 counter_Max,counter_trigg, debounce = 1):
        
        """
        Initialize the DCMotor class.
        
        Args:
            forward_pin (int): The GPIO pin number for the forward pin of the motor.
            back_pin (int): The GPIO pin number for the back pin of the motor.
            counter_pin (int): The GPIO pin number for the counter pin of the motor.
            lButton_pin (int): The GPIO pin number for the limit button pin of the motor.
            counter_PUD (int): The pull-up/down resistance setting for the counter pin.
            lButton_PUD (int): The pull-up/down resistance setting for the limit button pin.
            callback_name (function): The callback function to be executed when the counter pin state changes.
            counter_Max (int): The maximum value for the counter of the motor.
            counter_trigg (int): The triggering event for the callback function.
            debounce (int): The debounce time for the counter pin.
        """
        
        GPIO.setmode(GPIO.BCM)  # Set GPIO numbering mode to BCM
        GPIO.setwarnings(False) # Ignore warning messages
        
        # Assign passed parameters to class instance variables
        self.forward_pin=forward_pin
        self.back_pin=back_pin
        self.counter_pin=counter_pin
        self.lButton_pin=lButton_pin
        self.counter_pull_up_down=counter_PUD
        self.button_pull_up_down=lButton_PUD
        self.callback_name=callback_name
        self.counter_Max = counter_Max
        self.counter_trigg = counter_trigg
        self.debounce = debounce
        self.position_coordinate = 0
        
        self.direction = True # Initial direction
        self.counter=0 # Initial counter value
        
        self.run_robot = True # Initial setting for robot run
        
        # Set up GPIO pins for output or input as necessary
        GPIO.setup(self.forward_pin,GPIO.OUT)
        GPIO.setup(self.back_pin,GPIO.OUT)
        GPIO.setup(self.counter_pin,GPIO.IN,pull_up_down=counter_PUD)
        GPIO.setup(self.lButton_pin,GPIO.IN,pull_up_down=lButton_PUD)
        
        # Add an event detection on counter pin
        GPIO.add_event_detect(self.counter_pin,self.counter_trigg, callback=self.callback_name, bouncetime=self.debounce)
        
        # Initialize the forward and back pin as HIGH, motor is not running
        GPIO.output(self.forward_pin,GPIO.HIGH)
        GPIO.output(self.back_pin,GPIO.HIGH)

    # Method to return a string representation of the object    
    def __str__(self):
        return 'Motor control.' 
    
     # Method to move the DC motor backwards
    def back(self):
        if self.counter <= self.counter_Max:  # If the counter is less than or equal to max
            self.direction = True # Set the direction as True
            GPIO.output(self.forward_pin,GPIO.HIGH) # Set forward pin to HIGH
            GPIO.output(self.back_pin,GPIO.LOW) # Set back pin to LOW
            self.position_coordinate = self.counter # Set position coordinate to the counter
            time.sleep(0.01) # Wait for 0.01s
       

        else:
            self.stop() # Call stop method
            time.sleep(0.5) # Wait for 0.5s

    # Method to move the DC motor forward    
    def forward(self):
        if not GPIO.input(self.lButton_pin): # If the limit switch is not pressed
            self.direction = False # Set the direction as False
            GPIO.output(self.forward_pin,GPIO.LOW) # Set forward pin to LOW
            GPIO.output(self.back_pin,GPIO.HIGH) # Set back pin to HIGH
            self.position_coordinate = self.counter # Set position coordinate to the counter
            time.sleep(0.01) # Wait for 0.01s

        else:
            self.stop()
            time.sleep(0.5) # Wait for 0.5s 
            self.counter = 0 # Reset the counter to 0
            self.position_coordinate = self.counter # Reset position coordinate to the counter 
    
    # Method to stop the DC motor    
    def stop(self):
        GPIO.output(self.forward_pin,GPIO.HIGH)
        GPIO.output(self.back_pin,GPIO.HIGH)

    # Method to make the motor return to home position    
    def homing(self):
        while not GPIO.input(self.lButton_pin) and self.run_robot: # If the limit switch is not pressed and run_robot is True
            self.forward() # Call forward method to move the motor
        self.stop() # Call stop method
        time.sleep(0.5) # Wait for 0.5s
        if self.run_robot: # If the run_robot is True
            pass
            self.counter = 0 # Reset the counter to 0
            self.position_coordinate = self.counter  # Reset position coordinate to the counter 


    # Method to move the DC motor to a specified position
    def go_to_position(self,position):
        if self.counter < position: # If counter is less than target position
            while self.counter < position and self.run_robot: # While counter is less than target position and run_robot is True
                self.back() # Call back method to move the motor

            self.stop() # Call stop method
        elif self.counter > position: # If counter is more than target position
            while self.counter > position and self.run_robot: # While counter is more than target position and run_robot is True
                self.forward() # Call forward method to move the motor

            self.stop() # Call stop method


