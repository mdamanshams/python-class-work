class Parent():
    def __init__(self):
        self.name="Sheetal Ammar"
        self.age=34,39
        self.children=4
    def parenting(self):
        print("They are very good parent")
    def effort(self):
        print("They put their 100 percent ")
p1=Parent()
print(p1.name)
print(p1.age)
print(p1.children)
p1.parenting()
p1.effort()
p1.name="Mohak Malti"
print(p1.name)
class child(Parent):
    def effort(self):
        print("Their efforts has been reduced because their children is now grown ")
p1=child()
p1.effort()
del p1.children
print(p1.children)
