class Bottle:
    def __init__(self):
        self.name="Raja Ji"
        self.brand="Milton"
    def purpose(self):
        print("Bottles are used to store water.")
        print(self)
b=Bottle()
print(b.name)
print(b.brand)
b.purpose()
