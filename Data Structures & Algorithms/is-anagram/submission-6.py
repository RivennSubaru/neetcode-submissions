class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequence_s, frequence_t = [0] * 26, [0] * 26

        for chr_s in s:
            if "a" <= chr_s <= "z":
                frequence_s[ord(chr_s) - ord("a")] += 1
        
        for chr_t in t:
            if "a" <= chr_t <= "z":
                frequence_t[ord(chr_t) - ord("a")] += 1
        
        return frequence_s == frequence_t