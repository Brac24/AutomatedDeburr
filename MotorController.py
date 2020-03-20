#test
import serial
import signal
from threading import Timer #This is a better use as a timer than the python time library because we can interrupt this in case of an emergency



class MotorController:
    def __init__(self, name='motor'):
        self.name = name
        self.connection = serial.Serial("/dev/ttyUSB0")
        self.connection.baudrate = 115200
        

    def start_motor(self):  
        print('motor start')

    def emergency_stop(self):
        print("Emergency Stop")

    def stop_print(self):
        print('motor stop')


    @staticmethod
    def connect():
        """Connect to the motor controller serially (RS-232)"""
        try:
            se = serial.Serial("/dev/ttyUSB0")
            se.baudrate = 115200
        except serial.SerialException as error:
            print("Could not connect to motor controller " + error.__str__())



if __name__ == "__main__":
    print("hi")
    ser = serial.Serial("/dev/ttyUSB0")
    ser.baudrate = 115200
    ser.write('G91 A20\r\n'.encode('utf-8')) # Relative move of rotary
    ser.close()
