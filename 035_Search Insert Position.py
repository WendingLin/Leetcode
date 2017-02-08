#35. Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos=0
        while pos<len(nums):
            if target<=nums[pos]:
                return pos
            else:
                pos+=1
        return pos
