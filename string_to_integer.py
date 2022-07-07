#https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        numb_str = str()
        is_positive = True
        is_changed = False
        for item in s:
            if item == '+':
                if is_changed or numb_str:
                    break
                is_changed = True
                continue
            if item == '-':
                if is_changed or numb_str:
                    break
                is_changed = True
                is_positive = False
                continue
            if item.isdigit():
                numb_str +=item
            else:
                return self.checker(numb_str, is_positive)
        return self.checker(numb_str, is_positive)

    def checker(self, numb_str: str, is_positive: bool) -> int:
        if numb_str.isdigit():
            numb_int = int(numb_str)
            if not is_positive:
                numb_int *= -1
            if numb_int > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif numb_int < -2 ** 31:
                return -2 ** 31
            return numb_int
        return 0


s = Solution()
print(s.myAtoi(" asd    -42a1234"))
