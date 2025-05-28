
# Encapsulation

# Encapsulation refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class. It also restricts direct access to some components, which helps protect the integrity of the data and ensures proper usage.


class Employee:
    def __init__(self, name, salary):
        self.name = name                # public attribute
        self.__salary = salary          # private attribute

    # Getter method for salary (accessor)
    def get_salary(self):
        return self.__salary

    # Setter method for salary (mutator)
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount")

# Creating an employee object
emp = Employee("Alice", 50000)

# Accessing public attribute
print("Name:", emp.name)

# Accessing private attribute directly (will fail)
# print(emp.__salary)  # ❌ AttributeError

# Accessing private attribute using getter
print("Salary:", emp.get_salary())

# Modifying private attribute using setter
emp.set_salary(60000)
print("Updated Salary:", emp.get_salary())

# Trying to set invalid salary
emp.set_salary(-1000)  # ❌ Invalid salary amount
