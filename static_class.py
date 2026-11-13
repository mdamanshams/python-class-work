class car:
    def __init__(self):
        self.brand="BMW"
    def start(self):
        print("car is running")
    @staticmethod
    def move():
        print("car is moving")
    @classmethod
    def stop(cls):
        print("car is stopped")
c1=car()
print(c1.brand)
c1.start()
c1.move()
c1.stop()
car.move()
car.stop()
car.start() #here we will get error because we can not call a instance method we can only use reference variable