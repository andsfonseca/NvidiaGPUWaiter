

from .conditions.WhereConditions import WhereConditions
from .SMIParser import SMIParser

class AvailableGPU:

    @staticmethod
    def Any():
        gpus = SMIParser.getGPUs()

        if(len(gpus) == 0): 
            return -1
        else:
            return gpus[0].id
    
    @staticmethod
    def Where():
        """Retrieve the GPU number that meets the desired conditions. If nvidia-smi is not found the 
        default return value is 0.

        Parameters:
            condition (list[str]): Desired conditions.

        Returns:
            int: GPU number.
        """
        return WhereConditions(SMIParser.getGPUs())

# print(AvailableGPU.Where().NumberOfProcess().lessThan(30))
# print(AvailableGPU.Where().AvailableMemory().greaterThan(30))