class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        queue = collections.deque()

        for right, num in enumerate(nums):
            while queue and queue[-1] < num:
                queue.pop()

            queue.append(num)

            if right - left + 1 == k:
                res.append(queue[0])
                if nums[left] == queue[0]:
                    queue.popleft()
                
                left += 1
                

        return res        



