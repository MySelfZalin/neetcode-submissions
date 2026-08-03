class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check_k(k: int) -> bool:
            curr_hours = 0
            for pile in piles:
                curr_hours += math.ceil(pile / k)
                if curr_hours > h:
                    return False
            return True        


        
        max_val = max(piles)
        res = max_val
        left = 1
        right = max_val

        while left <= right:
            mid = (left+right) // 2
            if check_k(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res            