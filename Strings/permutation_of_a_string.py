val = "abc"

"""Using Recursion"""
def perm(arr, fi):
    if fi == len(arr)-1:
        print("".join(arr))
        return
    for i in range(fi, len(arr)):
        arr[i], arr[fi] = arr[fi], arr[i]
        perm(arr, fi+1)
        arr[i], arr[fi] = arr[fi], arr[i]


perm(list(val), 0)


"""Using Inbuilt"""
from itertools import permutations

perms = permutations(val)

for p in perms:
    print("".join(p))
