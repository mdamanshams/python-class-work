class mouse:
    def __init__(self):
        self.brand="logitek"
        self.cost=1000
    def move(self):
        print("mouse is for clicking")
m1=mouse()
print(m1.brand)
print(m1.cost)
m1.move()