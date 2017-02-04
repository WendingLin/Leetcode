#15.Three Sum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=list([])
        length=len(nums)
        for target in range(length-2):
            left=target+1; right=length-1
            while left < right:
                # Duplication Eliminating
                if target==0 or nums[target]>nums[target-1]:
                    if nums[left] + nums[right] == -nums[target]:
                        res.append(list([nums[target], nums[left], nums[right]]))
                        left+=1; right-=1
                        # Duplication Eliminating
                        while left<right and nums[left]==nums[left-1]: left+=1
                        while left<right and nums[right]==nums[right+1]: right-=1
                    elif nums[left]+nums[right]<-nums[target]:
                        while left<right:
                            left+=1
                            # Duplication Eliminating
                            if nums[left]!=nums[left-1]: break
                    else:
                        while left<right:
                            right-=1
                            # Duplication Eliminating
                            if nums[right]!=nums[right+1]: break
                else: break
        return res