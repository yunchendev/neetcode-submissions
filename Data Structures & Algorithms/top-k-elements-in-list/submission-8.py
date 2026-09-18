class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for val, freq in freqs.items():
            buckets[freq].append(val)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for val in buckets[i]:
                res.append(val)

                if len(res) == k:
                    return res