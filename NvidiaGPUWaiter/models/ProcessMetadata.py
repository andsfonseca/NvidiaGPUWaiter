class ProcessMetadata:
    """Set of information about the process using a gpu
    """

    def __init__(self, id):
        self.id = id
        """Process id using gpu."""
        self.type = "N/A"
        """Type of process"""
        self.name = ""
        """Name of process"""
        self.usedGPUMemory = None
        """Amount of memory used, if available"""