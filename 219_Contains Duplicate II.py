#219. Contains Duplicate II
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
    #My Solution
        # dict={}
        # for i in range(len(nums)):
        #     if nums[i] in dict and abs(dict[nums[i]]-i)<=k: return True
        #     else: dict[nums[i]]=i
        # return False
    #My Solution(Set)
        window=set([])
        for i in range(len(nums)):
            if i>k:
                window.discard(nums[i-k-1])
            if nums[i] in window:
                return True
            else:
                window.add(nums[i])
        return False
