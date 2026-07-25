class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            hash_val = self.get_hash(s)

            if hash_val in anagrams:
                anagrams[hash_val].append(s)
            else:
                anagrams[hash_val] = [s]
    
        return list(anagrams.values())
    
    def get_hash(self, string) -> str:
        str_set = sorted(set(list(string)))
        hash_val = []
        str_list = list(string)

        for char in str_set:
            hash_val.append(char)
            hash_val.append(str(str_list.count(char)))
        
        return "".join(hash_val)
                
