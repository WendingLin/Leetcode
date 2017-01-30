#4.Median of Two Sorted Arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #My Solution
        """
        length=len(nums1)+len(nums2)
        if(length%2==0):
            flag=1
            median=length/2
        else:
            flag=0
            median=(length+1)/2
        loca_nums1=loca_nums2=0
        value=0
        while loca_nums1+loca_nums2<median:
            if loca_nums1==len(nums1):
                value = nums2[loca_nums2]
                loca_nums2 = loca_nums2 + 1
            elif loca_nums2==len(nums2):
                value = nums1[loca_nums1]
                loca_nums1 = loca_nums1 + 1
            else:
                if nums1[loca_nums1]<nums2[loca_nums2]:
                    value = nums1[loca_nums1]
                    loca_nums1=loca_nums1+1
                else:
                    value=nums2[loca_nums2]
                    loca_nums2=loca_nums2+1
        if flag==0:
            return float(value)
        else:
            if loca_nums1 == len(nums1):
                value += nums2[loca_nums2]
            elif loca_nums2 == len(nums2):
                value += nums1[loca_nums1]
            else:
                if nums1[loca_nums1] < nums2[loca_nums2]:
                    value += nums1[loca_nums1]
                else:
                    value += nums2[loca_nums2]
            return float(value)/2.0
        """
        #Best Solution
        m, n=len(nums1), len(nums2)
        if m>n:
            nums1, nums2, m, n=nums2, nums1, n, m
        if n==0:
            raise ValueError
        imin, imax, half_len=0, m, (m+n+1)/2
        while imin<=imax:
            #Ensure the location of the median
            i=(imin+imax)/2
            j=half_len-i
            # i is too small, <m ensure not cross the border
            if i<m and nums2[j-1]>nums1[i]:
                imin=i+1
            # i is too large, >0 ensure not cross the border
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            # i is perfect
            else:
                if i==0: max_of_left=nums2[j-1]
                elif j==0: max_of_left=nums1[i-1]
                else: max_of_left=max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i==m: min_of_right=nums2[j]
                elif j==n: min_of_right=nums1[i]
                else: min_of_right=min(nums1[i], nums2[j])

                return(max_of_left+min_of_right)/2.0

