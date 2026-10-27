class phone:
	def __init__(self):
		self.name="xiaomi"
		self.type="feature phone"
		self.price=4500
	def purpose(self):
		print("To call or connect with persons.")
	def security(self):
		print("Security is top notch")
p=phone()
print(p.name)
print(p.type)
print(p.price)
p.purpose()
p.security()
p.sub_brand="Redmi"
print(p.sub_brand)
del p.type
print(p.type)