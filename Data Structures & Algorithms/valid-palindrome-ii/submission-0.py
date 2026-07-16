class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                lleft = left
                rright = right

                left += 1
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        right -= 1
                    else:
                        left = lleft
                        right = rright
                        right -= 1

                        while left < right:
                            if s[left] == s[right]:
                                left += 1
                                right -= 1
                            else:
                                return False    
                        return True        

                return True       



        return True        

        