#Create three classes, class A with the string “Hello ”, 
# class B with the string “World”,
#  and a class C with a method display() 
# that returns a concatenated string “Hello World”.

class A:
    str1 = "Hello"

class B:
    str2 = "World"

class C(A , B):
    def display(self):
        return  self.str1 + " " + self.str2

print (C().display())