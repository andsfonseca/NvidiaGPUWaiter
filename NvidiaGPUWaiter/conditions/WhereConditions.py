from .CountConditions import CountConditions

class WhereConditions():

    def __init__(self, gpus):
        self.gpus = gpus
        pass

    def NumberOfProcess(self):
        return CountConditions(list(map(lambda gpu: len(gpu.processes), self.gpus)))
    
    def AvailableMemory(self):
        return CountConditions(list(map(lambda gpu: gpu.memory.free, self.gpus)))
