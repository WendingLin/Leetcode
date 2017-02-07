#220. Contains Duplicate III



class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
    #My Solution
        if k<1 or t<0:
            return False
        import collections
        num_dict=collections.OrderedDict()
        for i in range(len(nums)):
            key=nums[i]/max(1, t)
            for m in (key, key-1, key+1):
                if m in num_dict and abs(num_dict[m]-nums[i])<=t:
                    return True
            num_dict[key]=nums[i]
            if i>=k:
                num_dict.popitem(last=False)
        return False