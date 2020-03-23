import serial
from MotorController import MotorController

class DeburrController:
    def __init__(self, name='deburr controller'):
        self.name = name
        self.motor_controller = None

    def startup(self):
        self.motor_controller = MotorController()
        error = self.motor_controller.connect()

        if error is not None:
            return error.__str__()

    def start_deburr(self):
        if self.motor_controller.is_connected:
            print('start deburr')
            self.motor_controller.start_motor()
        else:
            return 'Motor controller is not connected'
        