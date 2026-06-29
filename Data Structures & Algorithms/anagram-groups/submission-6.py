class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            char_frequency = [0] * 26

            for char in string:
                if "a" <= char <= "z":
                    char_frequency[ord(char) - ord("a")] += 1

            anagrams[",".join(str(nb) for nb in char_frequency)].append(string)
        
        return list(anagrams.values())