# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/0?selectedLang=python3

def findFloor(arr, x):
    n = len(arr)
    low, high = 0, n - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= x:
            ans = mid  
            low = mid + 1 
        else:
            high = mid - 1  
    return ans  
