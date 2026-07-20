class Solution:
    def isHappy(self, n: int) -> bool:
        happy = False
        num_list = [int(dig) for dig in list(str(n))]
        past_nums = []
        count = 0

        while happy == False:
            for num in num_list:
                count += num**2
            
            if count == 1:
                return True
            elif count in past_nums:
                return False
            else:
                past_nums.append(count)
                num_list = [int(dig) for dig in list(str(count))]
                count = 0





