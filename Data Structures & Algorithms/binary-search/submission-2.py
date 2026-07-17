class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right)//2
            
            print("before eval")
            print(left, right, mid)

            if left == right and nums[left] != target:
                return -1
            
            if left == right and nums[left] == target:
                return left
            
            temp = nums[mid]

            if temp == target:
                return mid
            
            elif target < temp:
                right = (mid) - 1

            elif target > temp:
                left = (mid) + 1

            print("after eval")
            print(left, right, mid)

        return -1
        
        


        
