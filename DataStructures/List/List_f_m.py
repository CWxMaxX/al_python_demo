# Built in List Functions and Methods

lst1 = []  # empty list
lst2 = ["Sunil", "Kamal", "Saman", "Rasika"]
lst3 = ["Sam", "Nadee", "Some", "Nuwan", "Zoysa", "Amal"]
lst4 = [20, 45, 75, 12, 35, 75, 24, 15, 95, 45]


print("Print Max Of list 4", max(lst4))
print("Print Max of list 3", max(lst3))
print("Print Min of list 4", min(lst4))
print("Print Min of list 3", min(lst3))
print('')

lst5 = list(("Sankar", "Susantha", "Priyal"))
print("list 5 = ", lst5)
print("")

print("List 1 = ", lst1)
lst1.append("Microsoft")
print("List 1 with append new word = ", lst1)
print()

countOf75 = lst4.count(75)
print("Count of 75 in List 4 = ", countOf75)
print()

lst2.extend(lst3)
print(lst2)
print()

indexOf45 = lst4.index(45)
print("Index of 45 in list 4 = ", indexOf45)
print()

lst3.insert(2, "CWx")
print("New List 3 =", lst3)
getObject2 = lst3.pop()
print("Last object of List 3 = ", getObject2)
print("New List 3 =", lst3)
getCwx = str(lst3.pop(2))
print("Without " + str(getCwx) + " = "+str(lst3))

lst4.remove(12)
print("After removing 12 from list 4 = ", lst4)

lst3.reverse()
print("Reverse list of List 3 = ", lst3)

lst4.sort()
print("Sort ", lst4)
lst4.sort(reverse=True)
print("Reverse sort ", lst4)
