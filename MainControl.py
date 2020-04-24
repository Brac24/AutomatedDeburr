from DeburrData import DeburrData
import time

class MainControl:
    """
    This class manipulates data as well as calls the classes that control physical hardware
    """
    def __init__(self):
        self.deburr_data = DeburrData()
        
    def startup(self):
        print('initialize main controller')

    def start(self, op_time):
        self.deburr_data.op_time = op_time
        self.deburr_data.current_time_left = op_time
        self.deburr_data.deburring_in_progress = True
        print("System Start")

    def stop(self):
        self.deburr_data.parts_deburred += 1 #Stop after successful deburr and increment parts deburred
        self.deburr_data.deburring_in_progress = False
        print("System Stop")
        time.sleep(.3) #sleep for half second before turning dc motors off to synchonize a bit with rotar
        return self.deburr_data.parts_deburred

    def update_elapsed(self):
        self.deburr_data.current_time_left -= 1 # decrement time left for operation
        return self.deburr_data.current_time_left

    def e_stop(self):
        print("E-STOP!!")
        self.deburr_data.current_time_left = 0
        self.deburr_data.deburring_in_progress = False
        return self.deburr_data.current_time_left

    def is_done(self):
        return (self.deburr_data.current_time_left == 0)

    def is_in_progress(self):
        return self.deburr_data.deburring_in_progress
