class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if n == 1:
            return nums[0]
            
        for i in range(n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return max(dp)