#33. Search in Rotated Sorted Array
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        if length==0:
            return -1
        left=0; right=length-1
        while left<right:
            if nums[left]==target:
                return left
            if nums[right]==target:
                return right

            mid=(left+right)//2
            if nums[mid]==target:
                return mid

            if nums[left]<nums[right]:
                if target<nums[left] or target>nums[right]:
                    return -1
                elif target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[left]>nums[mid]:
                if target>nums[mid] and target<nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[left]<target and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1

        if left==right and nums[left]!=target:
            return -1
        else:
            return left
S=Solution()
nums=[3,4,5,6,1,2]
S.search(nums, 7)




