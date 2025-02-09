#https://www.geeksforgeeks.org/problems/second-largest3735/1?page=1&category=Searching&sortBy

val = [1, 2, 3, 5, 4]

def getSecondLargest(arr):
    if len(arr)<2:
        return -1
    first = sec = float('-inf')
    for num in arr:
        if num > first:
            sec = first
            first = num
        elif num > sec and num != first:
            sec = num
    if sec == float('-inf'):
        return -1
    else:
        return sec

print(getSecondLargest(val))
