class Employee:
    company="ITC"
    name="defaultname"

    def show(self):
        print(f"the name is {self.name} and the salary is {self.company}")

class Coder:
    language="Python"
    def printlanguages(self):
        print(f"out of all the language here is your language:  {self.language}")
class Progameer(Employee,Coder):
    company="ITC Infotech"
    
    def showlanguage(self):
     print(f"the name is {self.name} and the is good with {self.language}")
 
a=Employee()
b=Progameer()
b.show()
b.printlanguages()
b.showlanguage()
print(a.company,b.company)