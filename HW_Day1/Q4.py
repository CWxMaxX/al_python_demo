arr = []
# To add data into list


def addDataToList():
    i = int(input("Mark : "))
    listOfMarks = []
    while i != -1:
        listOfMarks.append(i)
        i = int(input("Mark : "))

    return listOfMarks


# Call function
arr = addDataToList()
print(arr)

# To calculate maxium of list


def calculateMax(list):
    i = 0
    max = 0
    lengthOfList = len(list)
    while i < lengthOfList:
        if max < list[i]:
            max = list[i]
        i = i + 1
    print("Max = ", max)


# Call Function 2
calculateMax(arr)
