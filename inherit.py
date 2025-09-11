class employee:
    def __init__(self, name, salary):
        self.name = name
        
        self.salary = salary
    def display(self):
        print(f"Name:{self.name}, salary: {self.salary}")
class Manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        super().display()
        print(f"Department: {self.department}")
emp=employee("Virat Kohli", 50000)
emp.display()
mgr=Manager("Rohit Sharma", 100000, "Captain") 
mgr.display()                  