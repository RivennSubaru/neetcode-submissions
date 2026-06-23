class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hs, ht = {}, {}
        for i in range(len(s)):
            hs[s[i]] = 1 if s[i] not in hs else hs[s[i]] + 1
            ht[t[i]] = 1 if t[i] not in ht else ht[t[i]] + 1
        if hs == ht:
            return True
        else:
            return False