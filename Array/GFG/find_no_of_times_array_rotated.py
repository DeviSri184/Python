# https://www.geeksforgeeks.org/problems/rotation4723/1?page=1&category=Searching&sortBy

arr = [5, 1, 2, 3, 4]

"""Using inbuilt methods"""
def findKRotation(arr):
    least = min(arr)
    return arr.index(least)

"""Without inbuilt function"""
class Solution:
    def findKRotation(self, arr):
        first = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < first:
                return i
        return 0

print(Solution.findKRotation(arr)
