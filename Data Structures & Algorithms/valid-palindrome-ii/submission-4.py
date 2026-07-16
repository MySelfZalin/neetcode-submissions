class Solution: 
    def validPalindrome(self, s: str) -> bool:   
        
        def check_palidrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return check_palidrome(left + 1, right) or check_palidrome(left, right-1) 
        return True        
