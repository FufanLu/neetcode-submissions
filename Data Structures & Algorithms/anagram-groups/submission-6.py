class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in strs_map:
                strs_map[key].append(word)
            else:
                strs_map[key] = [word]
        
        return list(strs_map.values())
        