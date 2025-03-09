# https://www.geeksforgeeks.org/problems/wave-array-1587115621/1?selectedLang=python3


def convertToWave(arr):
    if len(arr) <= 1:
        arr = arr
    else:
        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]
