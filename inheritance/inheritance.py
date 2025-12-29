class Employee:
    company="ITC"

    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


class Progameer(Employee):
    company="ITC Infotech"
    
    def showlanguage(self):
     print(f"the name is {self.name} and the is good with {self.language}")

a=Employee()
b=Progameer()
print(a.company,b.company)