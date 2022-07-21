#https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        marget_list = sorted(nums1+nums2)
        if len(marget_list)%2 ==0:
            value = marget_list[len(marget_list)//2] + marget_list[len(marget_list)//2 -1]
            return value/2
        else:
            return float(marget_list[len(marget_list)//2])


s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2, 2]))
