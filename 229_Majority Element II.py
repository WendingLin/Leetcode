#229.Majority Element II
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #My Solution
        if len(nums)==0 or nums==None :
            return []
        elif len(nums)==1:
            return [nums[0]]
        else:
            majority_1, majority_2, count_1, count_2=nums[0], 0, 1, 0
            for i in range(0, len(nums)):
                if majority_1==nums[i]:
                    count_1+=1
                elif majority_2==nums[i]:
                    count_2+=1
                elif count_1==0:
                    majority_1, count_1=nums[i], 1
                elif count_2==0:
                    majority_2, count_2=nums[i], 1
                else:
                    count_1 -= 1
                    count_2 -= 1
            count_1=nums.count(majority_1)
            count_2=nums.count(majority_2)
            majority = list([])
            if count_1>len(nums)//3:
                majority.append(majority_1)
            if count_2>len(nums)//3 and majority_2!=majority_1:
                majority.append(majority_2)
            return majority

