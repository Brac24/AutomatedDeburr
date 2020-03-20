#test
import serial

class Motor:
	def __init__(self, name='motor'):
		self.name = name

	def start_motor():
        	print('motor start')



if __name__ == "__main__":
    print("hi")
    ser = serial.Serial("/dev/ttyUSB0")
    ser.baudrate = 115200
    ser.write('G91 A20\r\n'.encode('utf-8'))
    ser.close()
