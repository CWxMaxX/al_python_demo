i = 0
sum = 0
avg = 0

while i < 5:
    sum = sum + int(input("Enter Number " + str(i+1) + " : "))
    i = i + 1
avg = sum/5

print(avg)
