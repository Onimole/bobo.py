#Create three classes to show parent,
#  child, 
# and grandchild relationships.

class Parent:
    print("Parent Class")

class Child(Parent):
    print("Child Class")

class GrandChild(Child):
    print("Grand-Child class")

person =GrandChild()