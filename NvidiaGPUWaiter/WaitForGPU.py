from .AvailableGPU import AvailableGPU
import time

class WaitForGPU(AvailableGPU):
    
    @staticmethod
    def withCondition(condition = ["any"], seconds = 10.0):
        gpu = super(WaitForGPU, WaitForGPU).withCondition(condition)
        while(gpu == -1):
            time.sleep(seconds)
            gpu = super(WaitForGPU, WaitForGPU).withCondition(condition)

        return gpu