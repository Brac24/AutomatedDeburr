import serial
import threading
from gpiozero import LED
from MotorController import MotorController


class DeburrController:
    """
    This Controller contains hardware specific libraries for raspberry pi
    """
    def __init__(self, name='deburr controller'):
        self.name = name
        self.motor_controller = None
        

    def startup(self):
        """Initializes connection of main controller with the motor controller"""
        print('initializing deburr controller')

    def start_deburr(self, op_time):
        print('start deburr controller')

    def stop_deburr(self):
        print('stop deburr controller')

    def e_stop(self):
        print('deburr controller e-stop')
        
