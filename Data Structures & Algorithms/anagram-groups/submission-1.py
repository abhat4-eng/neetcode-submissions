class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            hash_val = [0] * 26

            for c in s:
                hash_val[ord(c) - ord("a")] += 1
            
            res[tuple(hash_val)].append(s)
        
        return list(res.values())

        