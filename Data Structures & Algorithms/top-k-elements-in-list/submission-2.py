class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {num: 0 for num in set(nums)}

        for num in nums:
            freqs[num] += 1

        buckets = [[] for num in set(nums)]

        maximum = max(list(freqs.values()))
        n = len(set(nums))

        for num in set(nums): 
            freq_val = freqs[num]
            bucket = int(
                (n * freq_val)/(maximum+1)
            )
            
            buckets[bucket].append(num)
        
        return [item for sublist in buckets for item in sublist][-1: -1 - k: -1]
        
        



