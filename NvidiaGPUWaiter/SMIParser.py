import subprocess

from .models.NvidiaGPU import NvidiaGPU
from .models.ProcessMetadata import ProcessMetadata
from .models.MemoryMetadata import MemoryMetadata

class SMIParser:

    @staticmethod
    def __getOutput():
        """Get the output of "nvidia-smi -q". If the service is not found, no value is returned

        Returns:
            list[str]: Output text.
        """
        try:
            sp = subprocess.Popen(['nvidia-smi', '-q'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = sp.communicate()
            return output[0].decode("utf-8").splitlines()
        except FileNotFoundError:
            return None
    
    @staticmethod
    def getGPUs():
        """Retrieves a list of available GPUs on the system.

         Returns:
            list[NvidiaGPU]: Gpus list.
        """
        lines = SMIParser.__getOutput()

        if lines is None:
            return []

        lineSeek = 0
        gpusFound = 0

        # Find Attached GPUs 
        for index in range(lineSeek, len(lines)):
            lineSeek = index
            line = lines[lineSeek]
            if "Attached GPUs" in line: 
                gpusFound = int(line.split(": ")[1])
                break
        
        # No GPU Found
        if gpusFound == 0:
            return []

        def nextLine(n = 1):
            nonlocal lineSeek
            lineSeek += n
            return lines[lineSeek]

        gpus = []
        currentGPUIndex = -1

        line = nextLine()

        while(lineSeek != len(lines)-1):
            
            if line.startswith('GPU'):
                currentGPUIndex += 1
                gpus.append(NvidiaGPU(currentGPUIndex))
                line = nextLine()

                continue
                
            if line.startswith('    Processes'):

                processes = []
                currentProcessIndex = -1
                line = nextLine()

                while(line.startswith('        ')):
                    if(line.startswith('        Process ID')):
                        currentProcessIndex += 1
                        id = int(line.split(": ")[1])
                        processes.append(ProcessMetadata(id))
                    elif(line.startswith('            Type')):
                        processes[currentProcessIndex].type = line.split(": ")[1]
                    elif(line.startswith('            Name')):
                        processes[currentProcessIndex].name = line.split(": ")[1]
                    elif(line.startswith('            Used GPU Memory')):
                        value = line.split(": ")[1]
                        if(value != "Not available in WDDM driver model"):
                            processes[currentProcessIndex].usedGPUMemory = int(value.split(" ")[0])

                    line = nextLine()

                ##Rollback Line
                line = nextLine(-1)
                
                gpus[currentGPUIndex].processes = processes

            elif line.startswith('    FB Memory Usage'):
                line = nextLine()
                memory = MemoryMetadata()
                while(line.startswith('        ')):

                    if(line.startswith('        Total')):
                        memory.total = int(line.split(": ")[1].split(" ")[0])
                    elif(line.startswith('        Used')):
                        memory.used = int(line.split(": ")[1].split(" ")[0])
                    elif(line.startswith('        Free')):
                        memory.free = int(line.split(": ")[1].split(" ")[0])

                    line = nextLine()

                ##Rollback Line
                line = nextLine(-1)

                gpus[currentGPUIndex].memory = memory

            line = nextLine()
        return gpus