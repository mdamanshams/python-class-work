class tv:
    def __init__(self):
        self.brand="lg"
        self.cost=800000
    def display(self):
        print("display is broken")
        print(self)
t1=tv()
print(t1.brand)
print(t1.cost)
t1.display()
print(t1)