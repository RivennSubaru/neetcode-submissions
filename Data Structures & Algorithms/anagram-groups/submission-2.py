class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g_annagrams = []
        seen = set()
        skip = 0
        dic1, dic2 = {}, {} 
        for i in range(len(strs)):
            if strs[i] not in seen:
                seen.add(strs[i])
                g_annagrams.insert(i - skip, [strs[i]])
                
                for j in range(i+1, len(strs)):
                    if len(strs[i]) == len(strs[j]):

                        for k in range(len(strs[i])):
                            dic1[strs[i][k]] = dic1.get(strs[i][k], 0) + 1
                            dic2[strs[j][k]] = dic2.get(strs[j][k], 0) + 1

                        if dic1 == dic2 :
                            seen.add(strs[j])
                            g_annagrams[i - skip].append(strs[j])
                        dic1.clear()
                        dic2.clear()
            else:
                skip += 1
        
        return g_annagrams