class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_res = 0
        cur_res = 0


        for num in nums:
            if num-1 not in nums_set:
                value = num
                while value in nums_set:
                    value += 1
                    cur_res += 1
                
                max_res = max(max_res, cur_res)
                cur_res = 0
        return max_res

