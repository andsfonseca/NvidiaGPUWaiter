class MemoryMetadata:
    """Set of information about the memory
    """
    
    def __init__(self):
        self.total = 0
        """Total gpu memory."""
        self.used = 0
        """Used gpu memory."""
        self.free = 0
        """Free gpu memory."""