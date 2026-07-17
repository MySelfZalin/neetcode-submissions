class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_res = 0
        while left < right:
            curr_res = (right - left) * min(heights[left], heights[right])
            max_res = max(max_res, curr_res)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_res            
        