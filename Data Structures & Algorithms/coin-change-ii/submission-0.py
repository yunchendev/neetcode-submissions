class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {} # (index, curr_amount)

        def backtrack(i, curr_amount):

            if (i, curr_amount) in dp:
                return dp[(i, curr_amount)]

            if curr_amount == amount:
                return 1
            if curr_amount > amount:
                return 0

            total = 0

            for j in range(i, len(coins)):
                total += backtrack(j, curr_amount + coins[j])

            
            dp[(i, curr_amount)] = total

            return total

            

        return backtrack(0, 0)