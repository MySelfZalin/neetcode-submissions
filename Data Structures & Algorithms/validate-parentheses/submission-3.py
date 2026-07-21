class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        association = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char not in association:
                stack.append(char)
            else:
                if not stack:
                    return False

                if association[char] != stack.pop():
                    return False

        return not bool(stack)                        
        