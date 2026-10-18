class phone:
    def __init__(self):
        self.brand="nokia"
        self.color="blue"
        self.price=1000
    def call(self):
        print("phone is ringing")
p1=phone()
print(p1.brand)
print(p1.color)
print(p1.price)
p1.call()