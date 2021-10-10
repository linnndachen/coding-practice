from typing import List


class Solution:
    def minCost2(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp, dp2 = {(0, 0): 0}, {}
        for i, a in enumerate(houses):
            for cj in (range(1, n + 1) if a == 0 else [a]):
                for ci, b in dp:
                    b2 = b + (ci != cj)
                    if b2 > target:
                        continue
                    dp2[cj, b2] = min(dp2.get((cj, b2), float('inf')),
                                      dp[ci, b] + (cost[i][cj - 1] if cj != a else 0))
            dp, dp2 = dp2, {}
        return min([dp[c, b] for c, b in dp if b == target] or [-1])

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {}

        # @functools.lru_cache(None)
        def dfs(i, groups, currentColor):
            # p
            key = (i, groups, currentColor)

            # base case, paint 0 houses
            if i == len(houses) or groups < 0 or m - i < groups:
                return 0 if groups == 0 and i == len(houses) else float('inf')

            if key not in dp:
                if houses[i] == 0:
                    dp[key] = min(dfs(i+1, groups - (newColor != currentColor), newColor) +
                                  cost[i][newColor - 1] for newColor in range(1, n + 1))
                else:
                    # painted before
                    dp[key] = dfs(i+1, groups - (houses[i] !=
                                                 currentColor), houses[i])

            return dp[key]

        res = dfs(0, target, -1)
        return res if res < float('inf') else -1
