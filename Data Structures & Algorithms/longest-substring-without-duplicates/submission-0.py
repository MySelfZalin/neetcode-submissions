class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

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
                seen_chars.remove(s[left])
                left += 1
                seen_chars.add(char)

        return max_res        






