# Inheritance in Python (OOP)

Inheritance is the ability to use **methods and attributes of an existing class** in a **newly created class**.

- **Super Class / Base Class / Parent Class** → The class being inherited from  
- **Derived Class / Sub Class / Child Class** → The class that inherits from the parent  

---

In Python, super().__init__() always calls the constructor of the next class in the Method Resolution Order (MRO),
 not necessarily just the “immediate” parent.

---
## Types of Inheritance in Python

1. **Single Inheritance**  
   - A child class inherits from **only one parent class**.  

2. **Multiple Inheritance**  
   - A derived class has **more than one parent class**.  
   - If parent classes have the same method, Python resolves it using **MRO (Method Resolution Order)**.  
   - Example:  
     ```python
     class Child(Mother, Father):
         pass

     print(Child.__mro__)  
     # Order: Child → Mother → Father → object
     ```

3. **Multilevel Inheritance**  
   - A chain of inheritance:  
   - `Grandparent → Parent → Child`

4. **Hierarchical Inheritance**  
   - Multiple child classes inherit from the **same parent class**.  
   - Example: Parent → Sibling1, Sibling2

5. **Hybrid Inheritance**  
   - A **combination** of two or more types of inheritance.

---

## Purpose of Inheritance
- **Removes code duplication**  
- Maintains a logical **relationship between objects**  

---

## Advantages
- Promotes **code reusability**  
- Eliminates **duplicate code**  
- Easy to **add new features**  
- Reduces **data redundancy**  
- Requires **less development effort**  
- Makes software **easy to maintain**

---

## Disadvantages
- Classes become **tightly coupled**  
  - A change in the **superclass** can directly affect the **subclass**  
- Parent and child classes may lose independence  

---