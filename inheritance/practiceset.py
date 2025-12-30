class twoD:
    def __init__(self,a,b):
        self.i=a
        self.j=b
    
class threeD(twoD):
   
    def __init__(self,a,b,c):
         super() .__init__(a,b)
         self.k=c
    def show(self):
        print(f"{self.i}i+{self.j}j+{self.k}k")

rohit=threeD(1,2,4)
rohit.show()

