
def multiplyMatrix(m1,m2): #m denotes matrix 
    pass

def vectorByMatrix(m,v): # FUNCTION IS VERY WRONG
    x = []
    for i in range(len(m.arr)):
        for y in range(len(v.vec)):
            m.arr[i][y] *= v.vec[y]
    for i in range(len(m.arr)):
        a = 0
        for y in range(len(v.vec)):
            a += m.arr[i][y]
        x.append(a)
    return x


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

    def ScalarByVector(self,Vector):
        for i in range(len(self.arr)):
            for y in range(len(Vector.vec)):
                self.arr[i][y] *= Vector.vec[y]
        
            
            

        

