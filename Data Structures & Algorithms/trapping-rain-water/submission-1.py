class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        res = 0

        left = 0
        right = len(height) - 1
        max_l = height[left]
        max_r = height[right]
        
        while left < right:
            if max_l < max_r:
                left += 1

                curr_height = max_l - height[left]
                res += max(0, curr_height)
                max_l = max(max_l, height[left])
            else:
                right -= 1

                curr_height = max_r - height[right]
                res += max(0, curr_height)     
                max_r = max(max_r, height[right])    

        return res
