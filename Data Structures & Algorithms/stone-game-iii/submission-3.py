class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            max_take = float('-inf')

            curr_stones_sum = 0

            for k in range(1, 4):
                if i + k <= n:
                    curr_stones_sum += stoneValue[i + k - 1]

                    max_take = max(max_take, curr_stones_sum - dp[i + k])

            dp[i] = max_take

        print(dp)

        if dp[0] == 0:
            return 'Tie'


        return 'Alice' if dp[0] > 0 else 'Bob'

