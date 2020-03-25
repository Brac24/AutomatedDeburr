import serial
from gpiozero import LED
from MotorController import MotorController
import time

class DeburrController:
    def __init__(self, name='deburr controller'):
        self.name = name
        self.motor_controller = None
        self.led = LED(17)

    def startup(self):
        """Initializes connection of main controller with the motor controller"""
        self.motor_controller = MotorController()
        error = self.motor_controller.connect()

        if error is not None:
            return error.__str__()

    def start_deburr(self):
        if self.motor_controller.is_connected:
            print('start deburr')
            self.led.on()
            self.motor_controller.start_motor()
            time.sleep(2)
            self.led.off()
            
        else:
            return 'Motor controller is not connected'
        