class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = list(str(x))
        if z == z[::-1]:
            return True
        return False


s = Solution()
print(s.isPalindrome(121))
