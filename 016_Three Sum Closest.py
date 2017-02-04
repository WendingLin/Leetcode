#16.Three Sum Closest
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        Min=1<<32-1
        length=len(nums)
        for i in range(length-2):
            if i>0 and nums[i]==nums[i-1]: continue
            left=i+1; right=length-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                Min=sum-target if abs(sum-target)<abs(Min) else Min
                if sum==target:
                    return target
                elif sum>target:
                    while left < right:
                        right -= 1
                        # Duplication Eliminating
                        if nums[right] != nums[right + 1]: break
                else:
                    while left < right:
                        left += 1
                        # Duplication Eliminating
                        if nums[left] != nums[left - 1]: break
        return Min+target