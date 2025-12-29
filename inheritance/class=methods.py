class Employee:
    a=1
    @classmethod#this gives that the value doesnot change for this particular function
    def showclassvalue(self):
        print(f"the value of a in class is: {self.a}")


e=Employee()
e.a=10
e.showclassvalue()