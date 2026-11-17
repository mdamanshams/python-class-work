class arithemtic:
    def __init__(self):
        pass
    def operation(self,a,b):
        c=a+b
        return c
    def operation2(self,a,b):
        c=a-b
        return c
    def operation3(self,a,b):
        c=a*b
        return c
    def operation4(self,a,b):
        c=a/b
        return c
a=arithemtic()
res1=a.operation(2,3)
print(res1)
res2=a.operation2(3,4)
print(res2)
res3=a.operation3(4,5)
print(res3)
res4=a.operation4(6,7)
print(res4)

