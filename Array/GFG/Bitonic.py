# https://www.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1?selectedLang=python3


def findMaximum(arr):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                return arr[mid]
            elif arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
