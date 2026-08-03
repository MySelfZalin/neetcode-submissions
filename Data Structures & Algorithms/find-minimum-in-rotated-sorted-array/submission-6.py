class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        min_res = nums[0]

        while l <= r:
            mid = (l + r) // 2
            min_res = min(min_res, nums[mid])
            if nums[r] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return min_res        