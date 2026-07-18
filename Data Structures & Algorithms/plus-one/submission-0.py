class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig_str = ""

        for dig in digits:
            dig_str += str(dig)
        
        new = str(int(dig_str)+1)

        return list(new)
        