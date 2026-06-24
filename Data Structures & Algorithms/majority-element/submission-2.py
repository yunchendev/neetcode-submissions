class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        for i, num in counter.items():
            if num > n / 2:
                return i

        return -1
