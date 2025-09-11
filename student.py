class Student:
    
    def __init__(self, name, roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, roll: {self.roll}, marks: {self.marks}")
s1=Student("Rohit Sharma", 45, 95)
s1.display()
s2=Student("Virat Kohli", 18, 94)
s2.display()        