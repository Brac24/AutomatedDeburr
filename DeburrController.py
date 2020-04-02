import serial
from gpiozero import LED
from MotorController import MotorController

class DeburrController:
    def __init__(self, name='deburr controller'):
        self.name = name
        self.motor_controller = None
        self.led = LED(17) #This is gpio 17 on raspberry pi 3B+ this will control a relay that will provide power to AC motors

    def startup(self):
        """Initializes connection of main controller with the motor controller"""
        self.motor_controller = MotorController()
        error = self.motor_controller.connect()

        if error is not None:
            return error.__str__()

    def start_deburr(self, op_time):
        if self.motor_controller.is_connected:
            print('start deburr')
            self.motor_controller.start_motor(op_time) #Starting turning rotary at a given velocity based on op cycle time
            self.led.on()           
        else:
            return 'Motor controller is not connected'

    def stop_deburr(self):
        print('stop deburr')
        self.led.off()
        self.motor_controller.stop_print()

        
