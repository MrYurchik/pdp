class Solution:
    def isHappy(self, n: int) -> bool:
        numb = list(str(n))
        numb_list = list()
        new_numb = 0
        while True:

            for item in numb:
                new_numb += int(item)**2
            print(new_numb)
            if new_numb in numb_list:
                return False
            numb_list.append(new_numb)
            if new_numb == 1:
                return True
            numb = list(str(new_numb))
            new_numb = 0


s = Solution()
print(s.isHappy(2))
