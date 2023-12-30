class Person:
    name=""
    age=""
        
    def _int_(self,name='',age=''):
         self.name=name
         self.age=age
         
class Employee(Person):
         def _int_(self,designation='',salary=''):
          super()._int_(self)
          self.designation=designation
          self.salary=salary                 
        
         def input(self):
          self.name=input("Enter name :")
          self.age=input("Enter age :")
          self.designation=input("Enter the designation :")
          self.salary=input("Enter the salary :")
         def show(self):
          print("Name:", self.name)
          print("Age:", self.age)
          print("Designation:", self.designation)
          print("Salary:", self.salary)
# Creating objects of the Employee class
obj=Employee()
obj1=Employee()
# Showing the record of the employees
obj.input()
obj.show()
print()
obj1.input()
obj1.show()