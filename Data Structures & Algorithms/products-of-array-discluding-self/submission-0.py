class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        val = 1
        for i in range(len(nums)):
            res.append(val)
            val *= nums[i]


        val = 1
        for i in reversed(range(len(nums))):
            res[i] *= val
            val *= nums[i]

        return res    
        
        