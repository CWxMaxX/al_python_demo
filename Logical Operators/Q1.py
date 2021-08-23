arr1 = [57, 28, 53, 77, 80]
arr2 = [62, 35, 70, 75, 63]


i = 0
count = len(arr1)
stList = []

# while i < count:
#     if arr1[i] > 60:
#         if arr2[i] > 60:
#             stNumber = "S" + str(i+1)
#             stList.append(stNumber)
#     i += 1


while i < count:
    if arr1[i] > 60 and arr2[i] > 60:
        stNumber = "S" + str(i+1)
        stList.append(stNumber)
    i += 1

print(stList)
