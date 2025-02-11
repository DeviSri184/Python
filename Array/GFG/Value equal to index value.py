# https://www.geeksforgeeks.org/problems/value-equal-to-index-value1330/1?page=2&category=Searching&sortBy

arr = [15, 2, 45, 4 , 7]


class Solution:
    def valueEqualToIndex(self, arr):
        result = []
        for i in range(len(arr)):
            if i+1 == arr[i]:
                result.append(arr[i])
        return result

"""same approach with diff syntax"""

def valueEqualToIndex(arr):
    return [item for idx, item in enumerate(arr) if idx+1 == item]
