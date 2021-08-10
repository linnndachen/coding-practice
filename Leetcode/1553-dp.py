
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n

        return 1 + min(n%2 + self.minDays(n//2), n%3+self.minDays(n//3))

"""
class Solution:
    def minDays(self, n: int) -> int:
        queue = deque([n])
        res = 0
        seen = set()
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                seen.add(node)

                if node == 0:
                    return res

                if node % 2 == 0:
                    val = node // 2
                    if val not in seen:
                        queue.append(val)

                if node % 3 == 0:
                    # 1-2/3 = 1/3
                    val = node//3
                    if val not in seen:
                        queue.append(val)

                if node - 1 not in seen:
                    queue.append(node-1)

            res += 1
"""