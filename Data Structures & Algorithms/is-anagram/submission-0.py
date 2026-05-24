class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}


        for l in s:
            if letters_s.get(l) is None:
                letters_s[l] = 1
            else:
                letters_s[l] += 1
        
        for l in t:
            if letters_t.get(l) is None:
                letters_t[l] = 1
            else:
                letters_t[l] += 1
        
        return letters_s == letters_t
            
