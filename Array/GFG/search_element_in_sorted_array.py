# https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?page=1&category=Searching&sortBy

"""Using Normal loop"""
class Solution:
    def searchInSorted(self,arr, k):
        for i in arr:
            if i == k:
                return True
        return False

"""Using list function """
class Solution:
    def searchInSorted(self,arr, k):
        if k in arr:
            return True
        return False


"""Using Binary Search"""
class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low+high) // 2
            print(mid)
            if arr[mid] == k:
                return True
            elif arr[mid] > k:
                high = mid-1
            else:
                low = mid+1
        return False

arr = [1, 2, 3, 4, 6]
k = 6

solu = Solution()
print(solu.searchInSorted(arr, k))


