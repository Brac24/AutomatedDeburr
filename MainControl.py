from DeburrData import DeburrData

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
        print("System Start")

    def stop(self):
        print("System Stop")

    def update_elapsed(self):
        pass

    def e_stop(self):
        print("E-STOP!!")
