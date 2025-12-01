#duplicate code
#without inheritance
#has repeated attributes and methods
"""class Faculty:
    def __init__(self,Fname,Lname,email,Fid,address,phone,teaching,salary,dateJoined):
        #converting attributes to objects
        self.Fname=Fname
        self.Lname=Lname
        self.email=email
        self.Fid=Fid
        self.address=address
        self.phone=phone
        self.teaching=teaching
        self.salary=salary
        self.dateJoined=dateJoined
    def getFullname(self):
        print(self.Fname+' '+self.Lname)
    def changeaddress(self,newaddress):
        self.address=newaddress
        print('address changed to',self.address)
    def changephone(self,newphone):
        self.phone=newphone
        print('phone changed to',self.phone)
    def getSalary(self):
        print('salary is',self.salary)
class Student:
    def __init__(self,Fname,Lname,email,Sid,address,phone,subjects,gpa,dateJoined):
        self.Fname=Fname
        self.Lname=Lname
        self.email=email
        self.Sid=Sid
        self.address=address
        self.phone=phone
        self.subjects=subjects
        self.gpa=gpa
        self.dateJoined=dateJoined
    def getFullname(self):
        print(self.Fname+' '+self.Lname)
    def changeaddress(self,newaddress):
        self.address=newaddress
        print('address changed to',self.address)
    def changephone(self,newphone):
        self.phone=newphone
        print('phone changed to',self.phone)
    def getGPA(self):
        print('gpa is',self.gpa) """

#removing duplicate code
#faculty and student -> members
# create a class called Member to remove duplicate code from both above classes
class Members:
    def __init__(self,Fname,Lname,email,Mid,address,phone,dateJoined):
        self.Fname=Fname
        self.Lname=Lname
        self.email=email
        self.Mid=Mid
        self.address=address
        self.phone=phone
        self.dateJoined=dateJoined
    def getFullname(self):
        print(self.Fname+' '+self.Lname)
    def changeaddress(self,newaddress):
        self.address=newaddress
        print('address changed to',self.address)
    def changephone(self,newphone):
        self.phone=newphone
        print('phone changed to',self.phone)


class Faculty(Members): #inherit Members class
    def __init__(self,Fname,Lname,email,Mid,address,phone,teaching,salary,dateJoined): #change Fid to Mid, also dont delete the parameters
        self.teaching=teaching
        self.salary=salary
        #calling Members class
        Members.__init__(self,Fname,Lname,email,Mid,address,phone,dateJoined) #imp observe ,we wrote "self"
    #removing common methods
    # can also super().__init__(...) instead of Members.__init__(self,...)
    def getSalary(self):
        print(self.salary) #use self.salary
# same goes for student class
class Student(Members):
    def __init__(self,Fname,Lname,email,Mid,address,phone,subjects,gpa,dateJoined): #Sid to Mid
        self.subjects=subjects
        self.gpa=gpa
        super().__init__(Fname,Lname,email,Mid,address,phone,dateJoined) # we didnt write "self" like we did for Members.__init__(self,..)
    def getGPA(self):
        print('gpa is',self.gpa)

f1 = Faculty("John", "Doe", "john@uni.com", 101, "NYC", "12345", "Math", 50000, "2020-01-01")
s1 = Student("Alice", "Smith", "alice@uni.com", 201, "LA", "67890", ["CS", "AI"], 3.8, "2021-08-20")  #see we used [..] for subject!!

f1.getFullname()   
f1.getSalary()     
s1.getFullname()   
s1.getGPA()        