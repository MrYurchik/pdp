#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        iter = 0
        sub_str = ''
        if len(s) == 1:
            return 1
        if not s:
            return 0
        while True:
            if s[iter] not in sub_str:
                sub_str += s[iter]
                iter +=1
            else:
                if length < len(sub_str):
                    length = len(sub_str)
                s = s[s.find(s[iter])+1:]
                sub_str = ''
                iter = 0

            if len(s) == iter:
                if len(sub_str) > length:
                    return len(sub_str)
                break
        return length

s = Solution()
print(s.lengthOfLongestSubstring("au"))
