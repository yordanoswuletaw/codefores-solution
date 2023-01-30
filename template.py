class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        self.arr = arr
        self.capacity = capacity
        self.length = length
   
    def insertEnd(self, value):
        if self.length < self.capacity:
            self.arr[self.length] = value 
            self.length += 1
        else:
             print('EOF')
       
    def removeEnd(self):
        if self.length:
            self.length -= 1
            self.arr[self.length] = 0
        else:
            print('Empty Array')
   
    def insertMiddle(self, index, value):
        # write your code here, you need to shift elements after insertion
        if 0 <= index < self.capacity and self.length < self.capacity:
            for i in range(self.length, index, -1):
                self.arr[i] = self.arr[i-1]
            self.arr[index] = value 
            self.length += 1
        else:
             print('Error')

       
    def removeMiddle(self, index):
        # write your code here, you need to shift elements after removal
        if 0 <= index < self.capacity and self.length:
            for i in range(index, self.length-1):
                self.arr[i] = self.arr[i+1]
            self.arr[self.length-1] = 0
            self.length -= 1
        else:
            print('Error')

   
    def printArr(self):
        for val in self.arr:
            yield val

arr = StaticArrays()
arr.insertEnd(4)
arr.insertEnd(5)
print(list(arr.printArr()))
arr.insertMiddle(1,6)
print(list(arr.printArr()))
arr.removeMiddle(2)
print(list(arr.printArr()))
arr.removeEnd()
print(list(arr.printArr()))
