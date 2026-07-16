class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        slovar = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in slovar:
                slovar[sorted_word] = []

            slovar[sorted_word].append(word)

        return list(slovar.values())

                
    
        