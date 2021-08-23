n = int(input("Input N : "))
a = 0

name = "Saman Perera"
name2 = 'Saman Perera'
name3 = """Saman Perera"""

while n > 0:
    x = int(input("Input X : "))
    if x % 2 == 0:
        a += 1
    n -= 1

print(a)
