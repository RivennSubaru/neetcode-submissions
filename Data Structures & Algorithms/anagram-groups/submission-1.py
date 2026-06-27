class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g_annagrams = []
        seen = set()
        skip = 0
        for i in range(len(strs)):
            if strs[i] not in seen:
                seen.add(strs[i])
                g_annagrams.insert(i - skip, [strs[i]])
                
                for j in range(i+1, len(strs)):
                    if len(strs[i]) == len(strs[j]):
                        hi, hj = {}, {}

                        for k in range(len(strs[i])):
                            hi[strs[i][k]] = hi.get(strs[i][k], 0) + 1
                            hj[strs[j][k]] = hj.get(strs[j][k], 0) + 1

                        if hi == hj :
                            seen.add(strs[j])
                            g_annagrams[i - skip].append(strs[j])
            else:
                skip += 1
        
        return g_annagrams