from collections import namedtuple


dict1 = {"Name": "Saman Perera", "Age": 26, "Tel": "0773725411"}
dict2 = {"Name": "Tharindu Madushan", "Age": 25, "Tel": "0773728659"}

print(dict1["Name"])
print(dict2)
print(str(dict2))

print("Length of dict1 =", len(dict1))

dict3 = dict1.copy()
print("Copiied", dict3)
print()

x = ('key1', 'key2', 'key3')
y = 0
subDict1 = dict.fromkeys(x, y)
print(subDict1)
print(dict1)

print(dict1.get("Name"))

xn = dict1.keys()
print("Keys of dict1 =", xn)

newDict1 = dict.fromkeys(xn)

print(newDict1)

itemsOfDict2 = dict2.items()
print(itemsOfDict2)
print()

dict5 = {"Country": "Sri Lanka"}

dict5.update(dict1)

print("Dict5 =", dict5)

print()
print(dict2.values())
