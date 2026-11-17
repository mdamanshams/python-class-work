class calsi:
    def operation(self,a,b):
        return a+b,a-b,a*b,a/b
c=calsi()
res1,res2,res3,res4=c.operation(10,20)
print(f"{res1} \n {res2} \n {res3} \n {res4} \n")