class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]

        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for j in range(1, len(grid)):
            dp[j][0] = dp[j - 1][0] + grid[j][0]

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                if dp[r - 1][c] < dp[r][c - 1]:
                    dp[r][c] = dp[r - 1][c] + grid[r][c]
                else:
                    dp[r][c] = dp[r][c - 1] + grid[r][c]

        return dp[len(grid) - 1][len(grid[0]) - 1]