
# Code BY JAPHETH C
class Employee:
    def __init__(self,full_name,role,salary):
        self.full_name = full_name
        self.role = role
        self.salary = salary

    def lastname(self):
        return self.full_name.split()[-1]

    def __repr__(self): # Operator Overloading, Without this or __str__ your class won't Print
            return "Employee: %s %s" % (self.full_name, self.salary)

# Inherits from Employee
class TechLead(Employee):
    # ------------------- Bad Augmentation Start -----------

    # def raiseSalary(self, percentage):
    #     self.salary = int(self.salary * (1 + percentage))  
    # ------------------ Bad Augmentation End ------------

    # ------------------- Good Augmentation -----------
    def raiseSalary(self,percentage,bonus=.15):
        self.salary = int(self.salary * (1 + percentage + bonus))


harry = Employee("Harry Styles", "Java Developer", 7000 )
print(harry)
Danny = TechLead("Danny Thom", "Tech Lead", 10000)
print(Danny)
print("****AFTER SALARY RAISE****")
Danny.raiseSalary(.15)
print(Danny)








