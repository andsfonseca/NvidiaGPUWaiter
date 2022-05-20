
import time

def WaitFor(method, seconds=10.0):
    """Put the current thread on hold until the value of the method sent returns a number greater 
    than or equal to 0. In the case of the GPU, wait until one has the required conditions

    Parameters:
        method (function): Method to be tested.
        seconds (float): seconds to wait.
    Returns:
        int: return of the method.
    """
    gpu = method()
    while(gpu == -1):
        time.sleep(seconds)
        gpu = method()
    return gpu