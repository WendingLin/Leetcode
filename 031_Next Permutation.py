#31.Next Permutation
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    #Steps:
    #1. Find two successive ascending elements from the trailer
    #2. Mark the first element as 'Partition'
    #3. Find another element larger than the 'Partition' element
    #4. Change the location of them
    #5. Sort the elements after the 'Partition' location in the reversed order
        loca_part=len(nums)-2
        while loca_part>-1:
            if nums[loca_part]<nums[loca_part+1]:
                break
            else:
                loca_part-=1
        if loca_part==-1:
            nums.reverse()
        else:
            for loca_change in range(len(nums)-1, loca_part, -1):
                if nums[loca_change]>nums[loca_part]:
                    nums[loca_change]+=nums[loca_part]
                    nums[loca_part]=nums[loca_change]-nums[loca_part]
                    nums[loca_change]=nums[loca_change]-nums[loca_part]
                    break
            nums[loca_part+1:]=list(reversed(nums[loca_part+1:]))
s=Solution()
nums=[1, 2, 3]
s.nextPermutation(nums)
print(nums)