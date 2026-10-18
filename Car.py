class Car:
    def __init__(self):
        self.brand="suzuki"
        self.color="blue"
        self.model="baleno"
    def on(self):
        print("Car is turning on")
    def run(self):
        print("Car is running")
    def off(self):
        print("Car is turning off")
c1=Car()
print(c1.brand)
print(c1.color)
print(c1.model)
c1.on()
c1.run()
c1.off()
