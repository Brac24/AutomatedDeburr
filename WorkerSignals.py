from PySide2.QtCore import QObject, Signal

class WorkerSignals(QObject):

    progress = Signal(int)