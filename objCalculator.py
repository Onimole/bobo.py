class Calculator:

    def __init__(self, a, b):
        self.aa = a
        self.bb = b

    def Addition(self):
        print (self.aa + self.bb)

    def Subtraction(self):
        print (self.aa - self.bb)

    def Multiplication(self):
        print (self.aa * self.bb)

    def Division(self):
        print (self.aa / self.bb)

obj = Calculator(1, 2)
obj.aa = float(input("Enter first number: "))
obj.bb = float(input("Enter second number: "))
print(obj.Addition())
print(obj.Subtraction())
print(obj.Division())
print(obj.Multiplication())


# print ("1. Addition")
# print ("2. Substraction")
# print ("3. Multiplication")
# print ("4. Division")

# while True:
#     choice = float(input("Enter your choice: ")) 
        
#     a = float(input("Enter the first number: "))
#     b = float(input("Enter the second number: "))


#     if choice == 1:
#         print(obj.Addition())
#     elif choice == 2:
#         print(obj.Subtraction())
#     elif choice == 3:
#         print(obj.Multiplication())
#     elif choice == 4:
#         print(obj.Division())    
#     break
# else:
#     print ("invalid output")