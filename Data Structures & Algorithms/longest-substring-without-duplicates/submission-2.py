class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_res = 0
        seen_chars = set()
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            if char not in seen_chars:
                seen_chars.add(char)
                max_res = max(max_res, len(seen_chars))
            else:
                while s[left] != char:
                    seen_chars.remove(s[left])
                    left += 1
                left += 1

        return max_res  
