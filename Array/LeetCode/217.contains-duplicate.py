# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

"""Another Approach"""
class Solution:
   def containsDuplicate(self, nums: List[int]) -> bool:
       if len(nums) == len(set(nums)):
           return False
       return True
