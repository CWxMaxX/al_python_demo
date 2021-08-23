# Find maximum number from inputs
# Stop when input -1


mark = 0
max = 0

while mark != -1:
    if max < mark:
        max = mark
    mark = int(input("Enter mark of student : "))
print("Max Mark = ", max)
