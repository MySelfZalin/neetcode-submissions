from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        res = 0
        maxFreq = 0

        for right, char in enumerate(s):
            count[char] += 1
            if count[char] > maxFreq:
                maxFreq = count[char]

            if right - left + 1 - maxFreq <= k:
                res = max(res, right-left+1) 
            else:
                while right - left + 1 - maxFreq > k:
                    count[s[left]] -= 1
                    left += 1
        return res            
                    
                      


