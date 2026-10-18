class Laptop():
    def __init__(self):
        self.brand = "Dell"
        self.modal = "G15"
        self.purpose ="Gaming"
    def working(self):
        print("Laptop is working perfectly")
    def performance(self):
        print("laptop is providing beast mode performance ")
l1 = Laptop()
print(l1.brand)
print(l1.modal)
print(l1.purpose)
l1.working()
l1.performance()
l1.purpose ="Other"
print(l1.purpose)
class child(Laptop):
    def performance(self):
        print("Now , Performance is decreased ")
l1 = child()
l1.performance()
del l1.brand
print(l1.brand)