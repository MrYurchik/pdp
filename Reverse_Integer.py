#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        str_int = str(x)
        if str_int[0] == '-':
            str_int =str_int[1:]
            str_int = '-' + str_int[::-1]
            if not self.checker(int(str_int)):
                return 0
            return int(str_int)
        if not self.checker(int(str_int[::-1])):
            return 0
        return int(str_int[::-1])

    def checker(self, x:int) -> bool:
        if -2**31 <= x <= 2**31 -1:
            return True
        return False


s = Solution()
print(s.reverse(2147483648))
