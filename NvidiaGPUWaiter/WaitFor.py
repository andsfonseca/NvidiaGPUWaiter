from .AvailableGPU import AvailableGPU
import time

class WaitForGPU(AvailableGPU):
    
    @staticmethod
    def withCondition(condition = ["any"], seconds = 10.0):
        """Retrieve the GPU number that meets the desired conditions. While not found, the current 
        thread will wait until the conditions are met. If nvidia-smi is not found the default 
        return value is 0.

        Parameters:
            condition (list[str]): Desired conditions.
            seconds (float): seconds to wait.
        Returns:
            int: GPU number.
        """
        gpu = super(WaitForGPU, WaitForGPU).withCondition(condition)
        while(gpu == -1):
            time.sleep(seconds)
            gpu = super(WaitForGPU, WaitForGPU).withCondition(condition)

        return gpu