from NvidiaGPUWaiter import WaitFor, AvailableGPU 

#AvailableGPU Example
print(AvailableGPU.Where().NumberOfProcess().lessThan(30))

#Wait for Example
print(WaitFor(lambda : AvailableGPU.Where().NumberOfProcess().lessThan(30)))