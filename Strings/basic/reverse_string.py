"""Using Slicing (Most Pythonic)"""

name = "GoodBeginning"
print(name[::-1])

"""Using loop"""

name = list("GoodBeginning")

size = len(name) - 1
length = len(name) // 2

for i in range(length):
    name[i], name[size-i] = name[size-i], name[i]

print("".join(name))



