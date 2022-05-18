import subprocess

class AvailableGPU:
    
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
    def withCondition(condition = ["any"]):
        """Retrieve the GPU number that meets the desired conditions. If nvidia-smi is not found the 
        default return value is 0.

        Parameters:
            condition (list[str]): Desired conditions.

        Returns:
            int: GPU number.
        """
        lines = AvailableGPU.__getOutput()

        if lines is None:
            return 0

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
            return -1

        def nextLine(n = 1):
            nonlocal lineSeek
            lineSeek += n
            return lines[lineSeek]

        currentGPU = -1
        line = nextLine()
        while(lineSeek != len(lines)-1):
            
            if line.startswith('GPU'):
                currentGPU += 1
                line = nextLine()
                continue
            
            if condition[0] == "any":
                return currentGPU
                
            elif condition[0] == "Number of process":
                if line.startswith('    Processes'):
                    count = 0
                    line = nextLine()

                    while(line.startswith('        ')):
                        
                        if(line.startswith('        Process ID')):
                            count +=1

                        line = nextLine()

                    if(condition[1] == "less than" and count < int(condition[2])):
                         return currentGPU

                    ##Rollback Line
                    line = nextLine(-1)
            elif condition[0] == "Available memory":
                if line.startswith('    FB Memory Usage'):
                    line = nextLine()
                    while(line.startswith('        ')):
                        if(line.startswith('        Free')):
                            value = int(line.split(": ")[1].split(" ")[0])
                            if(condition[1] == "less than" and value <  int(condition[2])):
                                return currentGPU
                        line = nextLine()

                    ##Rollback Line
                    line = nextLine(-1)

            line = nextLine()
        return -1