class NvidiaGPU:
    """Set of information about the gpu
    """
    
    def __init__(self, id):
        self.id = id
        """Identifier of GPU."""
        self.processes = []
        """Set of processes using the gpu."""
        self.memory = None
        """Memory information"""
        pass