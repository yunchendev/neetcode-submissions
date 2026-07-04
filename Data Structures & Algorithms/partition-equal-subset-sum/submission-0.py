class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        target = total_sum // 2 
        memo = {}


        def dp(index, curr_target):
            # base cases

            if curr_target == 0:
                return True
            if curr_target < 0 or index >= len(nums):
                return False

            # check memo

            if (index, curr_target) in memo:
                return memo[(index, curr_target)]
            
            # include or skip

            include = dp(index + 1, curr_target - nums[index])
            skip = dp(index + 1, curr_target)

            # save results
            memo[(index, curr_target)] = include or skip

            return memo[(index, curr_target)]

        return dp(0, target)