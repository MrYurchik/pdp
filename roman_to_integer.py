# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        integer = 0
        numb_comparison = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        for index, num in enumerate(s):
            if numb_comparison[s[index-1]] < numb_comparison[s[index]] and index-1 >= 0:
                continue
            if len(s) > index + 1:
                if numb_comparison[s[index]] >= numb_comparison[s[index+1]]:
                    integer += numb_comparison[s[index]]
                else:
                    integer += numb_comparison[s[index+1]] - numb_comparison[s[index]]
            else:
                integer += numb_comparison[s[index]]
        return integer

S = Solution()
S.romanToInt("MCMXCIV")