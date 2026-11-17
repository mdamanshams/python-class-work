class detergent:
    def __init__(self):
        self.brand="nirma"
        self.cost=100
    def wash(self, a,b):
        c=a/b
        return c
d1=detergent()
print(d1.brand)
print(d1.cost)
res=d1.wash(10,20)
print(res)
