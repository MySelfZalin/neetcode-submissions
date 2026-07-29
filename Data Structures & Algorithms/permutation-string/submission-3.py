from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dict_s1 = Counter(s1)

        left = 0
        match = 0
        dict_s2 = defaultdict(int)
        for right, char in enumerate(s2):
            dict_s2[char] += 1
            
            if char in dict_s1:
                if dict_s1[char] == dict_s2[char]:
                    match += 1

            

            if right - left + 1 > len(s1):
                left_char = s2[left]

                if left_char in dict_s1 and dict_s1[left_char] == dict_s2[left_char]:
                    match -= 1

                if dict_s2[left_char] > 1:
                    dict_s2[left_char] -= 1
                else:
                    del dict_s2[left_char]       
                left += 1

            if match == len(dict_s1):
                return True    

        return False    





        