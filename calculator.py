# making a simple calculator

def add (x,y):
    return x + y

def substract (x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division (x,y):
    return x / y

print("select operation.")
print("1. Add")
print("2.Substract")
print("3.Multiplication")
print("4.Division")

while True:
    choice = input("Enter your choice(1/2/3/4):")

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            print (num1, "+", num2, "=", add(num1,num2))

        elif choice == "2":
            print (num1, "-", num2, "=", substract(num1, num2))

        elif choice == "3":
            print (num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == "4":
            print (num1, "/", num2, "=", division(num1, num2))

        break

    else:
        print ("invalid input")