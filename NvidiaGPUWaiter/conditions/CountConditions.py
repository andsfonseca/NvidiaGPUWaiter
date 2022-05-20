class CountConditions:
    """Set of conditions related to numbers.

    Parameters:
        numbers (list[int]): Numbers to check.
    """
    
    def __init__(self, numbers):
        self.numbers = numbers
        pass

    def lessThan(self, value):
        """Returns the index that is less than the given value.

        Parameters:
            value (int): Value to be checked.

        Returns:
            int: index.
        """
        for i in range(len(self.numbers)):
            if(self.numbers[i] < value):
                return i
        return -1
    
    def greaterThan(self, value):
        """Returns the index that is greater than the given value.

        Parameters:
            value (int): Value to be checked.

        Returns:
            int: index.
        """
        for i in range(len(self.numbers)):
            if(self.numbers[i] > value):
                return i
        return -1