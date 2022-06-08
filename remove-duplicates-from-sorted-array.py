# Input:  nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
from typing import List

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

import time

def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
        return result

    return timed

# class Solution:
#     @timeit
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 0
#         while i < len(nums):
#             j = i + 1
#             while j < len(nums) and nums[j] == nums[i]:
#                 del nums[j]
#             i += 1
#
#         return len(nums)
#
#
# s = Solution()
# print(s.removeDuplicates(nums))
#

@timeit
def removeDuplicates(nums: List[int]) -> int:

    i = 0
    k = len(nums)
    while i < k:
        j = i + 1
        while j < k and nums[j] == nums[i]:
            del nums[j]
            k -=1
        i += 1
    return k


print(removeDuplicates(nums))