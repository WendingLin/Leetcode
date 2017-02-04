#18.Four Sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length=len(nums)
        res=[]
        if length<4: return res
        nums.sort()
        for i in range(length-3):
            if i>0 and nums[i]==nums[i-1]: continue
            for j in range(i+1, length-2):
                if j>i+1 and nums[j]==nums[j-1]: continue
                left = j + 1; right = length - 1
                while left<right:
                    sum=nums[i]+nums[j]+nums[left]+nums[right]
                    if sum==target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left +=1; right -= 1
                        while left<right and nums[left]==nums[left-1]: left+=1
                        while left<right and nums[right]==nums[right+1]: right-=1
                    elif sum>target:
                        while left<right:
                            right-=1
                            if nums[right]!=nums[right+1]:
                                break
                    else:
                        while left<right:
                            left+=1
                            if nums[left]!=nums[left-1]:
                                break
        return res