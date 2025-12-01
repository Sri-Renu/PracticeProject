# Example: Single, Multiple, and Multilevel Inheritance in Python

# Grandfather class (Base Class)
class Grandfather:  # no () means no inheritance
    def met1(self):
        print('grandfather')

# Parent1 inherits from Grandfather (Single Inheritance)
class Parent1(Grandfather):  # () means inheritance
    def met2(self):  # self = reference to current instance
        print('parent 1')

# Parent2 (independent class, no inheritance)
class Parent2:
    def met3(self):
        print('parent 2')

# Child inherits from both Parent1 and Parent2 (Multiple Inheritance)
# Also demonstrates Multilevel: Grandfather -> Parent1 -> Child
class Child(Parent1, Parent2):  
    def met4(self):
        print('child')

# Create object of Child
obj = Child()

# Access methods from all classes (due to inheritance chain)
obj.met1()  # From Grandfather (via Parent1)
obj.met2()  # From Parent1
obj.met3()  # From Parent2
obj.met4()  # From Child