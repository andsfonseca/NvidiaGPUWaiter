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

    def NumberOfComputeProcess(self, only=False):
        """Returns conditions related to the number of Compute (Type C) processes.

        Args:
            only (bool): Does not consider C+G type applications, i.e. programs that use both Compute Process and Graphics Process contexts at the same time
        Returns:
            CountConditions: conditions.
        """
        return CountConditions(list(map(lambda gpu: len(list(filter(lambda p: (p.type == 'C' or (not only and p.type == 'C+G')), gpu.processes))), self.gpus)))

    def NumberOfGraphicsProcess(self, only=False):
        """Returns conditions related to the number of Graphics (Type G) processes.

        Args:
            only (bool): Does not consider C+G type applications, i.e. programs that use both Compute Process and Graphics Process contexts at the same time
        Returns:
            CountConditions: conditions.
        """
        return CountConditions(list(map(lambda gpu: len(list(filter(lambda p: (p.type == 'G' or (not only and p.type == 'C+G')), gpu.processes))), self.gpus)))
    
    def AvailableMemory(self):
        """Returns conditions related to the available memory.

        Returns:
            CountConditions: conditions.
        """
        return CountConditions(list(map(lambda gpu: gpu.memory.free, self.gpus)))
