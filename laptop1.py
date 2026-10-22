class Laptop:
    def __init__(self):
        self.brand="hp"
        self.color="black"
    def display(self):
        self.type="oled"
        # type = "led"
l1=Laptop()
print(l1.brand)
print(l1.color)
l1.display()
print(l1.type)
l1.cost=40000
print(l1.cost)