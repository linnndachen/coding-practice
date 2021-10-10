from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        prev_min_cost = prev_sec_min_cost = prev_min_color = None

        for color, cost in enumerate(costs[0]):
            if prev_min_cost is None or cost < prev_min_cost:
                prev_sec_min_cost = prev_min_cost
                prev_min_color = color
                prev_min_cost = cost

            elif prev_sec_min_cost is None or cost < prev_sec_min_cost:
                prev_sec_min_cost = cost

        m, n = len(costs), len(costs[0])

        for house in range(1, m):
            min_cost = sec_min_cost = min_color = None

            for color in range(n):
                cost = costs[house][color]
                if color == prev_min_color:
                    cost += prev_sec_min_cost
                else:
                    cost += prev_min_cost

                if min_cost is None or cost < min_cost:
                    sec_min_cost = min_cost
                    min_color = color
                    min_cost = cost
                elif sec_min_cost is None or cost < sec_min_cost:
                    sec_min_cost = cost

            prev_min_cost = min_cost
            prev_min_color = min_color
            prev_sec_min_cost = sec_min_cost

        return prev_min_cost
