class Counter:
    def __init__(self) -> None:
        self.value = 0
        
    def increment_by_one(self):
        self.value =  self.value + 1
        return self.value
    
    def decrement_by_one(self):
        self.value =  self.value - 1
        return self.value
    
    def increment_by_n(self,n):
        self.value =  self.value + n
        return self.value
    
    def decrement_by_n(self,n):
        self.value =  self.value - n
        return self.value

counter = Counter()
counter.increment_by_one()
counter.decrement_by_one()
counter.increment_by_n(10)
counter.decrement_by_n(5)
print(counter.value)
