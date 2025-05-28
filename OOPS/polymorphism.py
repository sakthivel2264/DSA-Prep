
# Polymorphism
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print(self.fname, self.lname)
        
class Student(Person):
    pass 


class Staff(Person):
    def __init__(self, fname, lname, yearofJoin):
        super().__init__(fname, lname) # constructor chaining
        self.yearofJoin = yearofJoin
    
    def printName(self):  # method overriding (polymorphism)
        print(self.fname, self.lname, self.yearofJoin)
        
    def printName(self, age=20):  # method overloading
        print(self.fname, self.lname, self.yearofJoin, age)
    
    def awards(self, *args): # Simulating method overloading
        print(args)
    
    
S1 = Student("Sakthivel", "Pandiyan")
S2 = Staff("Sakthi", "Vel", 2021)

# S1.printName()
# S2.printName(20)
# S2.awards("Best Staff 2020", "Best Staff 2021")

for s in (S1, S2):
    s.printName() # Polymorphism