n = int(input("N : "))
a = 0

while n >= 0:
    x = int(input("X : "))
    if x % 2 == 0:
        a += 1
    n -= 1
print(a)
