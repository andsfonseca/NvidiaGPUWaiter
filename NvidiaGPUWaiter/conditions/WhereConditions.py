from .CountConditions import CountConditions

class WhereConditions():
    """Set of conditions related to gpu properties

    Parameters:
        numbers (list[gpus]): gpu list.
    """

    def __init__(self, gpus):
        self.gpus = gpus
        pass

    def NumberOfProcess(self):
        """Returns conditions related to the number of processes.

        Returns:
            CountConditions: conditions.
        """
        return CountConditions(list(map(lambda gpu: len(gpu.processes), self.gpus)))
    
    def AvailableMemory(self):
        """Returns conditions related to the available memory.

        Returns:
            CountConditions: conditions.
        """
        return CountConditions(list(map(lambda gpu: gpu.memory.free, self.gpus)))
