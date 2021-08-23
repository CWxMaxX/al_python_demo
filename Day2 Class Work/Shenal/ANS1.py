max = 0
x = 0
while x != -1:
    x = float(input("Enter a Mark : "))
    if max < x:
        max = x
print("Max =", '%.3f' % max)
