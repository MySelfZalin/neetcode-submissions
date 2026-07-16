class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for index, num in enumerate(nums):
            need = target - num
            if need in seen_nums:
                first_index = seen_nums[need]
                return [first_index, index]
            seen_nums[num] = index           