# Calculater

print("Calculater\nEnter 1 to '+'\nEnter 2 to '-'\nEnter 3 to '*'\nEnter 4 to '/'")

# Inputs
selector = int(input("Enter Operator Number : "))
x = float(input("Input first number = "))
y = float(input("Input second number = "))

# Custom Functions
# def addition(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def multi(x, y):
#     return x * y

# def divi(x, y):
#     return x / y

# ans = 0

if selector == 1:
    ans = x + y
elif selector == 2:
    ans = x-y
elif selector == 3:
    ans = x * y
elif selector == 4:
    ans = x / y
else:
    print("Operator selection error")

print("Answer = ", ans)
