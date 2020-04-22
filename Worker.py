from PySide2.QtCore import QRunnable, Slot
from WorkerSignals import WorkerSignals

class Worker(QRunnable):

    def __init__(self):
        super(Worker, self).__init__()

        self.signals = WorkerSignals()

    #@Slot
    #def run(self):
