import serial
from MotorController import MotorController

class DeburrController:
    def __init__(self, name='deburr controller'):
        self.name = name
        self.motor_controller = MotorController()
        self.motor_controller.connect()