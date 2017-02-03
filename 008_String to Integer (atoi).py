#8.String to Integer (atoi)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        """
        The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
        Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
        The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
        If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
        If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
        """
    #1.Strip the spacing
    #2.Scan the string and find the first digit or sign
        str=str.strip()
        if str=="":
            return 0
        length=len(str)
        value=0
        sign=1
        loca=0
        max_int=(1<<31)-1
        if str[loca]=='+':
            loca+=1
        elif str[loca]=='-':
            loca+=1
            sign=-1
        for loca in range(loca, length):
            if str[loca]<'0' or str[loca]>'9':
                break
            #In python there is no int boundary
            else:
                value=value*10+int(str[loca])
        value*=sign
        if sign==1 and value>max_int:
            value=max_int
        elif sign==-1 and value<-max_int-1:
            value=-max_int-1
        return value