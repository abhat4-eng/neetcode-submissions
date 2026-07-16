class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False

        split = list(s)
        empty = False
        dictionary = {"(": ")", "{": "}", "[": "]"}

        while empty == False:
            if split[0] in dictionary and split[1] == dictionary.get(split[0]):
                split.pop(0)
                split.pop(0)
            elif split[0] in dictionary and split[-1] == dictionary.get(split[0]):
                split.pop(0)
                split.pop()
            else:
                return False
            
            if not split:
                empty = True
        
        return True

        