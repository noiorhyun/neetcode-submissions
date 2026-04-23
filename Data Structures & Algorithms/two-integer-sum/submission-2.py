class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in pair:
                return[pair[diff], i]
            pair[num] = i

        
