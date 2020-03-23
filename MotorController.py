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
            ser.write('G0 X4\r\n'.encode('utf-8')) #Need to do an absolute move on any axis to be able to do relative moves
            ser.write('b!%\n'.encode('utf-8'))     #This line allows for the first command to complete else the command never ends. Don't know why maybe some end of line character or buffer bug
        except serial.SerialException as error:
            return 'Could not connect to motor controller ' + error.__str__()     


if __name__ == "__main__":
    print("hi")
    ser = serial.Serial("/dev/ttyUSB0")
    ser.baudrate = 115200
    ser.xonxoff = True
   # ser.rtscts = True
   # ser.reset_input_buffer()
   # ser.reset_output_buffer()
    
   # ser.write('G0 X4\r\n'.encode('utf-8'))
   # ser.write('b!%\n'.encode('utf-8'))
   # ser.write('\r\n'.encode('utf-8'))
    ser.write('G91 A2\r\n'.encode('utf-8'))  # Relative move of rotary
    ser.close()
