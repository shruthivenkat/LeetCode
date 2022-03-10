# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sub = 0
        max_sub = nums[0]
        for i in nums:
            if curr_sub < 0:
                curr_sub = 0 
            max_sub += i
            max_sub = max(max_sub, curr_sub)
        return max_sub

