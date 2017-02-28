
def add(x, y):
    """This function adds"""
    return x + y
def subtract(x, y):
    """This function subtracts"""
    return x - y
def multiply(x, y):
    """This function multiplies"""
    return x * y
def divide(x, y):
    """This function divides"""
    return x / y

#user input

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice (1/2/3/4):")

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))


if choice == "1":
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice =="4":
    print(num1, "/", num2, "=", divide(num1,num2))

else:
    print("invalid input")
