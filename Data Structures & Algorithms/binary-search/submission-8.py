class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right)//2

            temp = nums[mid]

            if temp == target:
                return mid
            
            elif target < temp:
                right = (mid) - 1

            elif target > temp:
                left = (mid) + 1

        return -1
        
        


        
