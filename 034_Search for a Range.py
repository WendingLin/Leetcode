#34. Search for a Range
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[-1, -1]
        length=len(nums)
        if length==0 or nums[length-1]<target or nums[0]>target:
            return res
        else:
            locastart=0
            locaend=length-1
            loca=int((locastart + locaend) / 2)

            while nums[loca]!=target:
                if locastart>locaend:
                    return res
                elif nums[loca]<target:
                    locastart=loca+1
                    loca=int((locastart + locaend) / 2)
                elif nums[loca]>target:
                    locaend=loca-1
                    loca = int((locastart+locaend)/2)
                elif locastart==locaend:
                    return res

            locastart=loca
            locaend=loca
            while locastart-1>=0 and nums[locastart-1]==target:
                locastart=locastart-1
            while locaend+1<=length-1 and nums[locaend+1]==target:
                locaend=locaend+1
            return [locastart, locaend]

s=Solution()
x=s.searchRange([1, 5],4)






