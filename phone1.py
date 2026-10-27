class phone:
	def __init__(self):
		self.name="Xoami"
		self.price=4500
	def purpose(self):
		print("It is for mainly connect with people through calling")
		print(self)
p=phone()
print(p.name)
print(p.price)
p.purpose()
p.name="Redmi"
print(p.purpose)
p.modal="keypad k1 pro"
print(p.modal)
del p.name
print(p.name)