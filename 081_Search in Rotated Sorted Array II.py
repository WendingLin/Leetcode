#81. Search in Rotated Sorted Array II
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length = len(nums)
        if length == 0 or nums==None:
            return False
        left = 0
        right = length - 1
        while left < right:
            if nums[left] == target:
                return True
            if nums[right] == target:
                return True
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] < nums[right]:
                if target < nums[left] or target > nums[right]:
                    return False
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if target > nums[mid] and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[left]<nums[mid]:
                if nums[left] < target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                left+=1

        if left == right and nums[left] != target:
            return False
        else:
            return True
S=Solution()
nums=[1,3,1,1,1]
S.search(nums, 3)