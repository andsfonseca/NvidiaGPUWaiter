class CountConditions:
    
    def __init__(self, numbers):
        self.numbers = numbers
        pass

    def lessThan(self, value):
        for i in range(len(self.numbers)):
            if(self.numbers[i] < value):
                return i
        return -1
    
    def greaterThan(self, value):
        for i in range(len(self.numbers)):
            if(self.numbers[i] > value):
                return i
        return -1