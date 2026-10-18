class City():
    def __init__(self):
        self.name="Bangluru"
        self.old=890
        self.population=8,443,675
    def popular(self):
        print("It is popular for its IT sector")
    def knownAs(self):
        print("It is also known as Silicon Valley of India")
c1=City()
print(c1.name)
print(c1.old)
print(c1.population)
c1.popular()
c1.knownAs()