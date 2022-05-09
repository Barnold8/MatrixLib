

class Matrix:

    def __init__(self,xdimensions,ydimensions,*numbers):
    
        self.arr = []
        f = 0 
        for i in range(ydimensions):
            self.arr.append([])
            for y in range(xdimensions):
                self.arr[i].append(numbers[f])
                f += 1
        
    
    def printMatrix(self):
        for i in range(len(self.arr)):
            print(self.arr[i])

    def vectorsToMatrix(self):
        pass

    def timesByVector(self,Vector):
        for i in range(len(self.arr)):
            for y in range(len(Vector.vec)):
                self.arr[i][y] *= Vector.vec[y]
        
            
            

        

