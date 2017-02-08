#167. Two Sum II - Input array is sorted
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0; right=len(numbers)-1
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [left+1, right+1]
            elif sum>target:
                right-=1
            else:
                left+=1