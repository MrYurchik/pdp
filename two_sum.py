# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for item in nums:
            if target - item != item:
                if target - item in nums:
                    return [nums.index(item), nums.index(target - item)]
            else:
                if len([i for i, x in enumerate(nums) if x == item]) > 1:
                    return [i for i, x in enumerate(nums) if x == item]


