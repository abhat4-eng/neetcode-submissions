class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        count = 0

        while True:
            while n:
                dig = n % 10
                count += (dig)**2
                n //= 10
            
            if count == 1:
                return True
            elif count in seen:
                return False
            else:
                seen.add(count)
                n = count
                count = 0






