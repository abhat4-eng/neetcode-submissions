class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        else:
            digits[-1] = 0
            current = -2

            while abs(current) <= len(digits):
                if digits[current] < 9:
                    digits[current] += 1
                    return digits
                
                else:
                    digits[current] = 0
                    current -= 1
            
            return [1] + digits
                
        