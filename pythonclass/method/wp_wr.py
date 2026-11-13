class calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1500
    def add(self , a,b):
        c=a+b
        return c
c1=calci()
print(c1.brand)
print(c1.cost)
res=c1.add(10,20)
print(res)