class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > f * d:
            return 0
        else:
            dp = [[] for _ in range(d)]
            for i in range(d):
                dp[i] = [0 for _ in range((i + 1) * f + 1)]

            for i in range(1, f + 1):
                dp[0][i] = 1

            for dice in range(1, d):
                for v in range(1, (dice + 1) * f + 1):
                    for face in range(1, f + 1):
                        if v - face < 0:
                            break
                        elif v - face > dice * f:
                            continue

                        dp[dice][v] += dp[dice - 1][v - face]
                        dp[dice][v] %= (1000000007)

                    if dice == d - 1 and v == target:
                        return dp[dice][v]

            return dp[0][target]