class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0 

        for num in nums:
            count = count + 1 if num == 1 else 0

            res = max(res, count)

        return res