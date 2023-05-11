# NvidiaGPUWaiter

NvidiaGPUWaiter is a package that detects idle GPUs with certain conditions using nvidia-smi.

## What is?

NvidiaGPUWaiter is a package designed to help you manage and monitor the usage of NVIDIA GPUs on your system. 

With NvidiaGPUWaiter, you can easily detect idle GPUs that meet specific conditions such as the number of processes, available memory, and types of processes. 

The package also allows you to wait for a GPU to become available and meet the specified conditions before executing a block of code.

## Installation
To install NvidiaGPUWaiter, you can use the following command:

```shell
pip install NvidiaGPUWaiter@git+https://github.com/andsfonseca/NvidiaGPUWaiter
```

## Usage

### Get Any GPU

Returns the first gpu found.

```python
print(AvailableGPU.Any())
```

### Get Any GPU with a condition

You can use the Where command to find the required conditions

#### Number of processes

Recovers the gpu with a number of processes less (or greater) than `n` processes.

```python
print(AvailableGPU.Where().NumberOfProcess().lessThan(n))
```

You can also use the `greaterThan()` command

```python
print(AvailableGPU.Where().NumberOfProcess().greaterThan(n))
```

#### Number of Compute processes (Type C)

Recovers the gpu with less (or greater) number of 'Compute' processes (Type C) than `n` processes.

```python
print(AvailableGPU.Where().NumberOfComputeProcess().lessThan(n))
```

If you want to ignore processes that have 'Compute' and 'Graphics' context (Type C+G). You can add only=True

```python
print(AvailableGPU.Where().NumberOfComputeProcess(only=True).lessThan(n))
```

#### Number of Graphics processes (Type G)

Recovers the gpu with less (or greater) number of 'Graphics' processes (Type G) than `n` processes.

```python
print(AvailableGPU.Where().NumberOfGraphicsProcess().lessThan(n))
```

If you want to ignore processes that have 'Compute' and 'Graphics' context (Type C+G). You can add only=True

```python
print(AvailableGPU.Where().NumberOfGraphicsProcess(only=True).lessThan(n))
```

#### Available memory

Recovers gpus that have `m` amount of available memory (in mb).

```python
print(AvailableGPU.Where().AvailableMemory().greaterThan(m))
```

### Wait until

Allows you to sleep your application until some condition is satisfied

```python
print(WaitFor(lambda : AvailableGPU.Where().NumberOfProcess().lessThan(n)))
```

## Examples

The following snippet shows a small example of how to use tensorflow to retrieve a gpu with specified conditions

```python
import tensorflow as tf
from NvidiaGPUWaiter import WaitFor, AvailableGPU

index = WaitFor( lambda: AvailableGPU.Where().NumberOfProcess().lessThan(1))
gpus = tf.config.list_physical_devices('GPU')
try:
    tf.config.set_visible_devices(gpus[index], 'GPU')
except RuntimeError as e:
    print(e)
```

## Issues

Feel free to submit issues and enhancement requests.

## Contribution

1. Fork the project
2. Create a _branch_ for your modification (`git checkout -b my-new-resource`)
3. Do the _commit_ (`git commit -am 'Adding a new resource...'`)
4. _Push_ (`git push origin my-new-resource`)
5. Create a new _Pull Request_ 

## License

NvidiaGPUWaiter is licensed under the MIT license.