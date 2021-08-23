arr1 = (67, 28, 63, 77, 80)
arr2 = (62, 35, 70, 75, 63)

# input(arr1,arr2)
count = len(arr1)
i = 0
stList = []

while i < count:
    if arr1[i] > 60:
        if arr2[i] > 60:
            stList.append("S"+str(i+1))
    i += 1
print(stList)
