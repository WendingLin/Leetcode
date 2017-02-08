#11. Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0; right=len(height)-1
        res=0
        while left<right:
        # Shrink from the shorter line
            res=max(res, (right-left)*min(height[left], height[right]))
            if height[left]<height[right]:
                k=left
                while left<right and height[k]>=height[left]:
                    left+=1
            else:
                k=right
                while left<right and height[k]>=height[right]:
                    right-=1
        return res





