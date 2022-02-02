# Solved on 2022. 2. 2.
# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        
        for i, n in enumerate(nums):
            if target - n in dictionary:
                return [dictionary[target-n], i]
            dictionary[n] = i