from PySide2.QtCore import QRunnable, Slot
from WorkerSignals import WorkerSignals

class Worker(QRunnable):

    def __init__(self, fn, *args):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args

    @Slot
    def run(self):
        self.fn(*self.args)
