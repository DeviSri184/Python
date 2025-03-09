# https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-arrays-with-duplicate-elements/1?selectedLang=python3

def intersection(self,a, b):
    a=set(a)
    b=set(b)
    m=a.intersection(b)
    return sorted(list(m))


def intersection(self,a, b):
    ans = []
    for i in a:
        if i in b:
            ans.append(i)
    return ans
