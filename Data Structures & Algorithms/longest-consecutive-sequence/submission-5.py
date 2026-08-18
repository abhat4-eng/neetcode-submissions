class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set: #2,20,4,10,3,5
            if (num - 1) not in num_set:
                current = num + 1
                run = 1
                while current in num_set:
                    current += 1
                    run += 1
                
                if run > longest:
                    longest = run
        
        return longest


