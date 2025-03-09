# https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1?selectedLang=python3


def segregate0and1(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] == 1:
            if arr[high] != 1:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
            else:
                high -= 1
        else:
            low += 1
    return arr
