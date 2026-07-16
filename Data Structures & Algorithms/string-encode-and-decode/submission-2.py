class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_val = []
        for word in strs:
            len_word = len(word)
            encoded_val.extend(list(str(len_word)))
            encoded_val.append('#')
            encoded_val.append(word)

        return "".join(encoded_val)    
            

    def decode(self, s: str) -> List[str]:

        

        res = []
        i = 0
        
        while i < len(s):
            digits = []
            while s[i] != '#':
                digits.append(s[i])
                i += 1
            i += 1

            world_len = int("".join(digits))
            res.append(s[i:i + world_len])
            i += world_len
        
        return res


            
