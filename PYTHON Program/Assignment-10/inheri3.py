
class Student:
     
        name = ""
        age = ""
    
class Sub(Student):   
        sub1 = ""
        sub2 = ""
    
        def input1(self):
        
         self.name=(input("Enter the name:"))
         self.age=(input("Enter your age: "))
         self.sub1=(input("Enter sub1: "))
         self.sub2=(input("Enter sub2: "))
        
        def ari(self):
         print("For Arts stu")
         print("name: ",self.name)
         print("age:",self.age)
         print("Subject 1:",self.sub1)
         print("Subject 2:",self.sub2)        
        
        def sci(self):
         print("name: ",self.name)
         print("age: ",self.age)
         print("For Science stu")   
         print("Subject 1:",self.sub1)
         print("Subject 2:",self.sub2) 

# Creating objects of the ScienceStudent and ArtStudent classes
obj=Sub()

# Showing the records of the students
print("Arts Student:")
obj.input1()
obj.ari()
print()
print("Science Student:")
obj.input1()
obj.sci()
