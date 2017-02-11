#66. Plus One
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        for i in range(0, len(digits))[::-1]:
            sum = carry+digits[i]
            if sum > 9:
                carry = 1
                digits[i] = 0
            else:
                carry = 0; digits[i]=sum
        if carry==1:
            digits.insert(0,1)
        return digits
