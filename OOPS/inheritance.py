
# Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print(self.fname, self.lname)
        
# Inherited
class Student(Person):
    pass 

# Inherited
class Staff(Person):
    def __init__(self, fname, lname, yearofJoin):
        super().__init__(fname, lname) # constructor chaining
        self.yearofJoin = yearofJoin
    
    def printName(self):
        print(self.fname, self.lname, self.yearofJoin)
        
    
    
S1 = Student("Sakthivel", "Pandiyan")
S2 = Staff("Sakthivel", "Pandiyan", 2021)

S1.printName()
S2.printName()