# test
import serial
import signal
# This is a better use as a timer than the python time library because we can interrupt this in case of an emergency
from threading import Timer
import time

class MotorController:
    is_connected = False
    serial_connection = None

    def __init__(self, name='motor'):
        self.name = name

    def start_motor(self, op_time):
        print('motor start')
        velocity = (360/int(op_time)) * 60 # degrees/min 1200 deg/min ~= 13s
        if velocity > 1200:
            print(f'velocity is {velocity}')
            MotorController.serial_connection.write(f'$avm {1200}\r\n'.encode('utf-8'))
        else:
            MotorController.serial_connection.write(f'$avm {velocity}\r\n'.encode('utf-8'))
        time.sleep(1)
        MotorController.serial_connection.write('G91 A360\r\n'.encode('utf-8'))
        time.sleep(1)
        print(MotorController.serial_connection.in_waiting)
        rcv = MotorController.serial_connection.read(MotorController.serial_connection.in_waiting)
        print(rcv.decode('utf-8'))
        while True:
            line = MotorController.serial_connection.readline()
            print(line.decode('utf-8'))
            time.sleep(.1)
            if not line:
                break
        #MotorController.serial_connection.write('b!%\n'.encode('utf-8'))     #This line allows for the first command to complete else the command never ends. Don't know why maybe some end of line character or buffer bug

    def emergency_stop(self):
        print("Emergency Stop")
        MotorController.serial_connection.write('! \r\n'.encode('utf-8'))
        time.sleep(1)
        MotorController.serial_connection.write('\x18 \r\n'.encode('utf-8'))

    def stop_print(self):
        print('motor stop')
        data_bytes = MotorController.serial_connection.in_waiting
        print(data_bytes)
        rcv = MotorController.serial_connection.read(data_bytes)
        print(rcv.decode('utf-8'))

    @staticmethod
    def connect():
        """Connect to the motor controller serially (RS-232)"""
        try:
            MotorController.serial_connection = serial.Serial("/dev/ttyUSB0")
            MotorController.serial_connection.timeout = 1
            MotorController.serial_connection.baudrate = 115200
            MotorController.serial_connection.xonxoff = True
            MotorController.serial_connection.stopbits = serial.STOPBITS_ONE
            MotorController.serial_connection.parity = serial.PARITY_NONE
            MotorController.serial_connection.bytesize = serial.EIGHTBITS
            MotorController.is_connected = True
            MotorController.serial_connection.write('G0 X4\r\n'.encode('utf-8')) #Need to do an absolute move on any axis to be able to do relative moves
            MotorController.serial_connection.write('b!%\n'.encode('utf-8'))     #This line allows for the first command to complete else the command never ends. Don't know why maybe some end of line character or buffer bug
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
