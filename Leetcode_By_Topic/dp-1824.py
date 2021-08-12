class Solution:
    def minSideJumps(self, obstacles):
        dp = [float('inf'), 0, float('inf')]

        for lane in obstacles:
            if lane == 0:
                dp = [min(dp[1]+1, dp[2]+1, dp[0]),
                      min(dp[0]+1, dp[2]+1, dp[1]),
                      min(dp[0]+1, dp[1]+1, dp[2])]
            else:
                if lane == 1:
                    dp[0] = float('inf')
                    dp[1] = min(dp[1], dp[2]+1)
                    dp[2] = min(dp[2], dp[1]+1)
                elif lane == 2:
                    dp[0] = min(dp[0], dp[2]+1)
                    dp[1] = float('inf')
                    dp[2] = min(dp[0]+1, dp[2])
                else:
                    dp[0] = min(dp[1]+1, dp[0])
                    dp[1] = min(dp[0]+1, dp[1])
                    dp[2] = float('inf')

        return min(dp)

    """
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[0] * (4) for _ in range(n)]

        dp[0][2] = 0
        dp[0][1] = dp[0][3] = 1

        for i in range(1, n):
            obs = obstacles[i]
            minVal = float('inf')

            for j in range(1, 4):
                if j == obs:
                    dp[i][j] = float('inf')

                else:
                    dp[i][j] = dp[i-1][j]
                
                minVal = min(minVal, dp[i][j])
                
            for j in range(1, 4):
                if j != obs and dp[i][j] != minVal:
                    dp[i][j] = minVal + 1

        res = float('inf')
        for j in range(1, 4):
            res = min(res, dp[n-1][j])

        return res
    """
