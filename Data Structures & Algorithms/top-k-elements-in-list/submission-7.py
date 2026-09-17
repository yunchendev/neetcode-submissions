class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first get frequency 

        freq = {}   
        res = []
        for num in nums:
            if num not in freq:
                freq[num] = 0

            freq[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for val, freq in freq.items():
            buckets[freq].append(val)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res