from multiprocessing import Process
from multiprocessing import Condition, Lock
from multiprocessing import Value
from multiprocessing import current_process

class Monitor():
    def __init__(self):
        self.mutex = Lock()
        self.nthinking = Value ('i',0)
        self.neating = Value ('i',0)
        