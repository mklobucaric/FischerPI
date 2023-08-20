import RPi.GPIO as GPIO
import time
class DCMotor():
    def __init__(self,forward_pin,back_pin,counter_pin,lButton_pin,counter_PUD,lButton_PUD,callback_name,
                 counter_Max,counter_trigg, debounce = 1):
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
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
        
        self.direction = True
        self.counter=0
        
        self.run_robot = True
        
        GPIO.setup(self.forward_pin,GPIO.OUT)
        GPIO.setup(self.back_pin,GPIO.OUT)
        GPIO.setup(self.counter_pin,GPIO.IN,pull_up_down=counter_PUD)
        GPIO.setup(self.lButton_pin,GPIO.IN,pull_up_down=lButton_PUD)
        
        GPIO.add_event_detect(self.counter_pin,self.counter_trigg, callback=self.callback_name, bouncetime=self.debounce)
        
        GPIO.output(self.forward_pin,GPIO.HIGH)
        GPIO.output(self.back_pin,GPIO.HIGH)
        
    def __str__(self):
        return 'Upravljanje motorom.' 
    
    def back(self):
        if self.counter <= self.counter_Max: 
            self.direction = True
            GPIO.output(self.forward_pin,GPIO.HIGH)
            GPIO.output(self.back_pin,GPIO.LOW)
            self.position_coordinate = self.counter
            time.sleep(0.01)

            

        else:
            self.stop()
            time.sleep(0.5)     
        
    def forward(self):
        if not GPIO.input(self.lButton_pin):
            self.direction = False
            GPIO.output(self.forward_pin,GPIO.LOW)
            GPIO.output(self.back_pin,GPIO.HIGH)
            self.position_coordinate = self.counter
            time.sleep(0.01)

        else:
            self.stop()
            time.sleep(0.5)
            self.counter = 0
            self.position_coordinate = self.counter
        
    def stop(self):
        GPIO.output(self.forward_pin,GPIO.HIGH)
        GPIO.output(self.back_pin,GPIO.HIGH)

        
    def homing(self):
        while not GPIO.input(self.lButton_pin) and self.run_robot:
            self.forward()
        self.stop()
        time.sleep(0.5)
        if self.run_robot:
            pass
            self.counter = 0
            self.position_coordinate = self.counter 
    
    def go_to_position(self,position):
        if self.counter < position:
            while self.counter < position and self.run_robot:
                self.back()


            self.stop()
        elif self.counter > position:
            while self.counter > position and self.run_robot:
                self.forward()

            self.stop()


