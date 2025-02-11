# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?page=1&category=Searching&sortBy

"""Loop Approach"""
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2

def countFreq(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count += 1
    return count


print(countFreq(arr, target))


"""List count"""

def countFreq(arr, target):
    return arr.count(target)

print(countFreq(arr, target))


"""Inbuilt module"""

from collections import Counter


def countFreq(arr, target):
    freq = Counter(arr)
    return freq[target]

print(countFreq(arr, target))




