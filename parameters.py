class demo:
    #this parameter is called as formal parameter
    def disp(self,a=10,b=20,c=30):
        print(a)
        print(b)
        print(c)
d=demo()
x=11
y=22
z=33
d.disp()
#these type of parameter is called as actual
d.disp(x)
d.disp(x,y)
d.disp(z)
d.disp(y,z,x)
d.disp(c=z)
d.disp(a=z,b=y,c=x)
