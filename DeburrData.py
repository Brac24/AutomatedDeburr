class DeburrData:
    def __init__(self):
        self.part_number = ""
        self.job = ""
        self.operation = ""
        self.op_time = 0           # total time required for operation to complete
        self.current_time_left = 0 # this value gets decremented as the timer from GUI is triggered
        self.parts_deburred = 0    # current parts deburred
        self.deburring_in_progress = False