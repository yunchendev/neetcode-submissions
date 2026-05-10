class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {
            1: 1,
            2: 2
        }
        
        def helper(n):
            if n in cache:
                return cache[n]

            else:
                cache[n] = helper(n - 1) + helper(n - 2)

            return cache[n]

        return helper(n)