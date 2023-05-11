from NvidiaGPUWaiter import WaitFor, AvailableGPU 

#AvailableGPU Example
print(AvailableGPU.Where().NumberOfProcess().greaterThan(30))
print(AvailableGPU.Where().AvailableMemory().greaterThan(1000))

print(AvailableGPU.Where().NumberOfComputeProcess().lessThan(30))
print(AvailableGPU.Where().NumberOfComputeProcess(only=True).lessThan(30))

print(AvailableGPU.Where().NumberOfGraphicsProcess().lessThan(30))
print(AvailableGPU.Where().NumberOfGraphicsProcess(only=True).lessThan(30))

#Wait for Example
print(WaitFor(lambda : AvailableGPU.Where().NumberOfProcess().lessThan(30)))