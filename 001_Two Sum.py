#1.Two Sum
class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #ON2
        """
        loca_a=0
        loca_b=1
        flag=0
        while loca_a<len(nums):
            loca_b=loca_a+1
            while loca_b<len(nums) :
                if nums[loca_a]+nums[loca_b]==target:
                    flag=1
                    break
                else:
                    loca_b+=1
            if flag==1:
                break
            else:
                loca_a+=1
        return [loca_a,loca_b]
        """
        #ON
        dict={}
        for loca in range(len(nums)):
            if nums[loca] in dict:
                return [dict[nums[loca]], loca]
            else:
                dict[target-nums[loca]]=loca

