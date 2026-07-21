class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        assotiation = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char not in assotiation:
                stack.append(char)
            else:
                if not stack:
                    return False

                if assotiation[char] != stack.pop():
                    return False
        if stack:
            return False
        else:
            return True                                
        