class Employee:
    a=1
    @classmethod#this gives that the value doesnot change for this particular function
    def showclassvalue(self):
        print(f"the value of a in class is: {self.a}")
    
    @property
    def name(self):
        return(f"{self.fname} {self.lname}")
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]




e=Employee()
e.name="harry khan"
print(e.name)
e.a=10
e.showclassvalue()