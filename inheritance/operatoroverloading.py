class Number:
    def __init__(self,n):
        self.number=n
    def __add__(self,num):
        return self.number+num.number

n1=Number(1)
n2=Number(2)
print(n1+n2)
