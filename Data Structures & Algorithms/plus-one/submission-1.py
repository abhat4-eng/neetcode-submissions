class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig_str = ""

        for dig in digits:
            dig_str += str(dig)
        
      #  new = [int(dig) for dig in str(int(dig_str)+1)]

        return [int(dig) for dig in str(int(dig_str)+1)]
        