lst1 = []  # empty list
lst2 = ["Sunil", "Kamal", "Saman", "Rasika"]
lst3 = ["Sam", "Nadee", "Some", "Priyanga", "Nuwan"]

print("Printing methods of list")
print(lst2)
print(*lst2)
print(*lst2, sep="/")
print(*lst2, sep="\n")
print("Basic Operations")
print("Length of list = ", len(lst2))
print('')
print(lst2 + lst3)
print('')
print(lst2*4)
print('')
print("Is Kamal in list 2 ? ", ("Kamal" in lst2))
print("Is Kamal in list 3 ? ", ("Kamal" in lst3))
print('')

print("Print list using for loop")
for x in lst2:
    print(x, end=",")
