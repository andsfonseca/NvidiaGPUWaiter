

from .conditions.WhereConditions import WhereConditions
from .SMIParser import SMIParser

class AvailableGPU:

    @staticmethod
    def Any():
        """Retrieve any GPU number found. If nvidia-smi is not found, the default return value 
        is -1.

        Returns:
            int: GPU number.
        """
        gpus = SMIParser.getGPUs()

        if(len(gpus) == 0): 
            return -1
        
        return 0
    
    @staticmethod
    def Where():
        """Retrieve the GPU number that meets a condition. If nvidia-smi is not found, the default 
        return value is -1;

        Returns:
            int: GPU number.
        """
        return WhereConditions(SMIParser.getGPUs())