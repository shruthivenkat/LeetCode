class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for i, num in enumerate(nums):
            potential_match = target - num
            if potential_match in num_hash:
                return [num_hash[potential_match], i]
            num_hash[num] = i