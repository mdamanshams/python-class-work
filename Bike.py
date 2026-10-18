class Bike :
    def __init__(self):
        self.brand="Hero"
        self.modal="Glamour"
        self.price=150000
    def on(self):
        print("Bike starting")
    def running(self):
        print("Bike is running")
    def off(self):
        print("bike is off")
b1=Bike()
print(b1.brand)
print(b1.modal)
print(b1.price)
b1.on()
b1.running()
b1.off()
b1.brand="Hero Honda"
print(b1.brand)
#process of method override
class Child(Bike):
    def running(self):  # Overrides Bike.running
        print("Bike has broken down")
b1=Child()
b1.running()
del b1.brand
print(b1.brand)

