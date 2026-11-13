class Jai:
    def __init__(self):
        self.name = "jai"
        self.gender="men"
        self.age=28
    def quality(self):
        print("He is a good programer")

    def personality(self):
        print("He is very desi")
        print(self)
j=Jai()
print(j.name)
print(j.age)
print(j.gender)
j.quality()
j.personality()