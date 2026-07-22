class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[-1] * m for _ in range(n)]

        print(memo)


        def dfs(i, j):




            if i == n - 1 and j == m - 1 and obstacleGrid[i][j] != 1:
                return 1

            if i >= n or j >= m or obstacleGrid[i][j] == 1:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = dfs(i + 1, j) + dfs(i, j + 1)

            return memo[i][j]

        return dfs(0, 0)
