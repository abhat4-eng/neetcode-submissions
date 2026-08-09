class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            if nums.count(0) > 1:
                return [0] * len(nums)

            prod = 0
            other_prod = 1
            for num in nums:
                if num != 0:
                    other_prod = other_prod * num
            
            return [0 if num != 0 else other_prod for num in nums]
        
        else:
            prod = 1
            for num in nums:
                prod = prod * num

            return [int(prod/num) for num in nums]    


