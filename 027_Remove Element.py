#27.Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length=len(nums)
        loca=0
        while loca<length:
            if nums[loca]==val:
                del nums[loca]
                length-=1
            else:
                loca+=1
        return length