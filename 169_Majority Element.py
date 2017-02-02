#169.Majority Element
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # My Solution
        majority, count = nums[0], 1
        for i in range(1, len(nums)):
            if majority == nums[i]:
                count += 1
            elif count == 0:
                majority, count = nums[i], 1
            else:
                count -= 1
        return majority

