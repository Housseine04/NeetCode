class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = {}
        for str in strs:
            occurs = [0]*26
            for l in str:
                occurs[ord(l) - ord('a')] += 1
            key = tuple(occurs)
            if not key in mappings:
                mappings[key] = []
            mappings[key].append(str)
        
        result= []
        for key in mappings:
            result.append(mappings[key])
        return result