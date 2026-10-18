class heroin :
    def __init__(self):
        self.name="kajal"
        self.age=50
    def dance(self):
        print("kajal is a good dancer")
h1=heroin()
print(h1.name)
print(h1.age)
h1.dance()
h1.movie="dheera"
print(h1.movie)
h1.age=55
print("new age")
del h1.age
print(h1.age)