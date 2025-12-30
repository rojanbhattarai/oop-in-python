class Vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def __add__(self,vector):
        return Vector(self.i+vector.i , self.j+vector.j)
    def __mul__(self,vector):
        return Vector(self.i*vector.i , self.j*vector.j)

    def show(self):
        print(f"the vector is : {self.i}i + {self.j}k")

rohit=Vector(1,2)
rojan=Vector(3,4)
hancy=rohit+rojan
hancymax=rohit*rojan
hancy.show()
hancymax.show()
