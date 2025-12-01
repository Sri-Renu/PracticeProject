# POLYMORPHISM

class A:
    def add(self,*args):
        if args:
            result=type(args[0])() #can't use sum coz its bult-in function (not a bug, but best avoided).
            for i in args:  
                result+=i
            return result

obj=A()
print(obj.add(1,2)) # 2 int
print(obj.add(1,2,3))  # 3 int
print(obj.add(12.3,4.5,6.7)) # float
print(obj.add('a','b'))
print(obj.add('a','b','c'))
print(obj.add(1,2,3.4,5.6))  # int + float
print(obj.add([1,2],[3,4]))

"""result = type(args[0])() — what's happening?

args[0] is the first argument.
type(args[0]) gets its type (e.g., int, float, str, list).
Adding () creates a default empty value of that type.

If first arg is int → int() → 0
If first arg is float → float() → 0.0
If first arg is str → str() → '' (empty string)
If first arg is list → list() → []"""