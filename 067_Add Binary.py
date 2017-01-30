#67.Add Binary
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    #Direct Binary Addition (Slower)
        """
        carry=0
        value=""
        index_a=len(a)-1
        index_b=len(b)-1
        while index_a>=0 or index_b>=0:
            x=int(a[index_a]) if index_a>=0 else 0
            y=int(b[index_b]) if index_b>=0 else 0
            if x+y+carry==0:
                value='0'+value
                carry=0
            elif x+y+carry==1:
                value='1'+value
                carry=0
            elif x+y+carry==2:
                value='0'+value
                carry=1
            else:
                value = '1' + value
                carry=1
            index_a=index_a-1
            index_b=index_b-1
        if carry==1:
            value = '1' + value
            return value
        else:
            return value
        """
    #Direct Decimal Addition
        #int(str,base) will be faster
        """
        value=0
        step=0
        for loca in range(len(a)-1, -1, -1):
            if  a[loca]=='1':
                value+=pow(2, step)
            step+=1
        step=0
        for loca in range(len(b)-1, -1, -1):
            if b[loca]=='1':
                value+=pow(2, step)
            step+=1
        return bin(value)[2:] #Index of String
        """
    #Best Solution
        if len(a) == 0: return b
        if len(b) == 0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'

s=Solution()
print(s.addBinary("1111", "1111"))