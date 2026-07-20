class Solution:
    def trap(self, height: List[int]) -> int:


        res = 0

        left = 0
        right = len(height) - 1
        max_l = height[left]
        max_r = height[right]
        
        while left < right:
            if height[left] < height[right]:
                left += 1
                max_l = max(max_l, height[left])
                res += max_l - height[left]
            else:
                right -= 1
                max_r = max(max_r, height[right])
                res += max_r - height[right]

        return res
