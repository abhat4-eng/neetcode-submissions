class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        current = nums

        while not found:

            if (len(current) == 1 and current[0] != target) or not current:
                return -1
            
            if len(current) == 1 and current[0] == target:
                return nums.index(current[0])
            
            temp = current[len(current)//2]

            if temp == target:
                return nums.index(temp)
            
            elif target < temp:
                current = current[: (len(current)//2)]

            elif target > temp:
                current = current[(len(current)//2) + 1:]
            
            print(current)

        
        


        
