from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        # sort by efficiency, then use heap have fastest k-1 speed

        data = sorted(zip(efficiency, speed), reverse=True)

        heap, speedSum, res = [], 0, 0

        for i in range(n):
            eff, speed = data[i]

            if len(heap) > k-1:
                speedSum -= heapq.heappop(heap)

            speedSum += speed
            res = max(res, speedSum * eff)

            heapq.heappush(heap, speed)

        M = 10**9 + 7
        return res % M