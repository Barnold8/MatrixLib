
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

def vectorsToMatrix():
    pass

class Matrix:

    def __init__(self,xdimensions,ydimensions,*numbers):
        self.xDim = xdimensions
        self.yDim = ydimensions
        self.arr = []
        f = 0 
        for i in range(self.yDim ):
            self.arr.append([])
            for y in range(self.xDim):
                self.arr[i].append(numbers[f])
                f += 1
        
    
    def printMatrix(self):
        for i in range(len(self.arr)):
            print(self.arr[i])

    def ScalarByVector(self,Vector):
        for i in range(len(self.arr)):
            for y in range(len(Vector.vec)):
                self.arr[i][y] *= Vector.vec[y]
        
    def det2(self): 
        if(len(self.arr)!= 2):
            print("This function is meant for a 2x2 matrix when a "+ str(self.xDim)+"x"+str(self.yDim)+" matrix was given")
            return
        return self.arr[0][0]*self.arr[1][1] - self.arr[0][1]*self.arr[1][0]            

    def det3(self):
        m1 = Matrix(2,2,self.arr[1][1],self.arr[1][2],self.arr[2][1],self.arr[2][2])
        m2 = Matrix(2,2,self.arr[0][1],self.arr[2][1],self.arr[0][2],self.arr[2][2])
        m3 = Matrix(2,2,self.arr[0][1],self.arr[1][1],self.arr[0][2],self.arr[1][2])
        if(len(self.arr)!= 3):
            print("This function is meant for a 3x3 matrix when a "+ str(self.xDim)+"x"+str(self.yDim)+" matrix was given")
            return
        return self.arr[0][0]*m1.det2() - self.arr[1][0]*m2.det2() + self.arr[2][0]*m3.det2()
        #https://www.symbolab.com/solver/matrix-determinant-calculator/%5Cdet%20%5Cbegin%7Bpmatrix%7D1%20%26%202%20%26%203%20%5C%5C4%20%26%205%20%26%206%20%5C%5C7%20%26%208%20%26%209%5Cend%7Bpmatrix%7D?or=ex
