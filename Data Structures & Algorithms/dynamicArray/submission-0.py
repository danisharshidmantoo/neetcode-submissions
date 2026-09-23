class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Darray = [float('inf')]*self.capacity
        self.end = 0
    def get(self, i: int) -> int:
        return self.Darray[i]

    def set(self, i: int, n: int) -> None:
        self.Darray[i] = n

    def pushback(self, n: int) -> None:
        if self.end<= self.capacity-1:
            self.Darray[self.end] = n
            self.end += 1
        else:
            self.resize()
            self.Darray[self.end] = n
            self.end += 1
    def popback(self) -> int:
        el = self.Darray[self.end-1]
        self.end -= 1
        return el

    def resize(self) -> None:
        self.capacity *= 2
        newArray = []
        for i in range(len(self.Darray)):
            newArray.append(self.Darray[i])
        for i in range(len(self.Darray)):
            newArray.append(float('inf'))
        self.Darray = newArray
    def getSize(self) -> int:
        return self.end
    
    def getCapacity(self) -> int:
        return self.capacity