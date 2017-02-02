#17.Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
    #My Solution
        length=len(digits)
        if length==0:
            return []
        dictLetter = {0: ' ', 1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        num=int(digits[0])
        letter=dictLetter[num]
        result=[]
        arr=[]

        for l in letter:
            if length>1:
                arr=self.letterCombinations(digits[1:])
                for a in arr:
                    result.append(l+a)
            else:
                result.append(l)

        return result


