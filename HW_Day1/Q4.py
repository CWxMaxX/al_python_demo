arr = [34, 23, 65, 78, 43]
i = 0
max = 0
lengthOfList = len(arr)
while i < lengthOfList:
    if max < arr[i]:
        max = arr[i]
    i = i + 1
print(max)
