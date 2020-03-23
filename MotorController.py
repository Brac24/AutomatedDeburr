# test
import serial
import signal
# This is a better use as a timer than the python time library because we can interrupt this in case of an emergency
from threading import Timer


class MotorController:
    is_connected = False
    serial_connection = None

    def __init__(self, name='motor'):
        self.name = name

    def start_motor(self):
        print('motor start')
        MotorController.serial_connection.write('G91 A20\r\n'.encode('utf-8'))

    def emergency_stop(self):
        print("Emergency Stop")

    def stop_print(self):
        print('motor stop')

    @staticmethod
    def connect():
        """Connect to the motor controller serially (RS-232)"""
        try:
            MotorController.serial_connection = serial.Serial("/dev/ttyUSB0")
            MotorController.serial_connection.baudrate = 115200
            MotorController.is_connected = True
        except serial.SerialException as error:
            return 'Could not connect to motor controller ' + error.__str__()     


if __name__ == "__main__":
    print("hi")
    ser = serial.Serial("/dev/ttyUSB0")
    ser.baudrate = 115200
    ser.write('G91 A20\r\n'.encode('utf-8'))  # Relative move of rotary
    ser.close()
