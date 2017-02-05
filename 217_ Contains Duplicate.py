#217. Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    #Set Solution
        #return len(set(nums)) != len(nums)
    #Sort Solution
        # nums.sort()
        # length=len(nums)
        # for i in range(length-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False
