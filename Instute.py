class student_info():
    def __init__(self):
        self.institute ="Pentagon"
        self.name ="Aman"
        self.course="Data Science"
        self.fees= 38000
    def information(self):
        print("\n student information............... ")
        print("student name : ",self.name)
        print("Institute :", self.institute)
        print("Course : ",self.course)
        print("Fees : ",self.fees)
        print("Aman is performing very poor ")
s1 = student_info()
print(s1.institute)
print(s1.name)
print(s1.course)
print(s1.fees)
s1.information()
s1.course= "Updated course : Data Analyst"
print(s1.course)
del s1.course
print(s1.course)