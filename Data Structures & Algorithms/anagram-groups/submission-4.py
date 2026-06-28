class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_h = {}
        anagrams_group = []

        for string in strs:
            sorted_string = sorted(list(string))
            key = "".join(sorted_string)
            anagram_h[key] = anagram_h.get(key, []) + [string]
        
        for anagrams in anagram_h.values():
            anagrams_group.append(anagrams)

        return anagrams_group