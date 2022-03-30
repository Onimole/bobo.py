#Create three classes A, B, and C.
#  Class A with attribute num=20. 
# Classes B and C should have the same properties as A 
# and also should be empty. 
# Create an instance of C and print the attribute num.

class A:
    num = 20

class B(A):
    pass

class C(A):
    pass

instance = C()
print(instance.num)
