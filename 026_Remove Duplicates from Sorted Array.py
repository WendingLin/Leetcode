#26. Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        for i in range(length):
            if i==length-1:
                return length
            while nums[i+1]==nums[i]:
               del nums[i+1]
               length-=1
               if i == length - 1:
                   return length