# Basic summation of vector functions
def addVectors(*vectors):
    v = Vector()
    maxDimension = 0

    for vec in vectors:
        if maxDimension < vec.getDimensions():
            maxDimension = vec.getDimensions()
    
    v.vec = [0]*maxDimension

    for vec in vectors:
        for i in range(len(vec.vec)):
            v.vec[i] += vec.vec[i]
            
    return v

def divVectors(*vectors):
    v = Vector()
    maxDimension = 0

    for vec in vectors:
        if maxDimension < vec.getDimensions():
            maxDimension = vec.getDimensions()
    
    v.vec = [0]*maxDimension

    for vec in vectors:
        for i in range(len(vec.vec)):
            v.vec[i] /= vec.vec[i]
            
    return v

def subVectors(*vectors):
    v = Vector()
    maxDimension = 0

    for vec in vectors:
        if maxDimension < vec.getDimensions():
            maxDimension = vec.getDimensions()
    
    v.vec = [0]*maxDimension

    for vec in vectors:
        for i in range(len(vec.vec)):
            v.vec[i] -= vec.vec[i]
            
    return v

def mulVectors(*vectors):
    v = Vector()
    maxDimension = 0

    for vec in vectors:
        if maxDimension < vec.getDimensions():
            maxDimension = vec.getDimensions()
    
    v.vec = [0]*maxDimension

    for vec in vectors:
        for i in range(len(vec.vec)):
            v.vec[i] *= vec.vec[i]
            
    return v

def dotProduct(*vectors): # assuming all vectors are of the same length
    maxDIM = vectors[0].getDimensions()
    x = [1]*maxDIM
    for v in vectors:
        if v.getDimensions() > maxDIM:
            print("This function needs all vectors to be of the same size")
            return
    for i in range(len(vectors)):
        for y in range(len(vectors[i].vec)):
            x[y] *= vectors[i].vec[y]
    return x
    
# Basic summation of vector functions


def transform(ihat,jhat,vector): # only works as a simple 2 length vector function right now
    x = vector.vec[0]
    y = vector.vec[1]
    return addVectors(ihat.scalar(x),jhat.scalar(y))

class Vector:

    def __init__(self,*numbers):
        self.vec = []
        for num in numbers:
            self.vec.append(num)

    def printVector(self):
        for num in self.vec:
            print(f"[{num}]".format())
            
    def getDimensions(self):
        return len(self.vec)

    def scalar(self,number):
        for i in range(len(self.vec)):
            self.vec[i] = self.vec[i] * number


