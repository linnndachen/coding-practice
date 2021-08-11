import collections
from typing import List
class Solution:
    def __init__(self):
        self.res = 0
        self.visited = collections.defaultdict(int)

    def numSquarefulPerms(self, nums: List[int]) -> int:
        nums.sort()
        graph, n = collections.defaultdict(list), len(nums)

        # build ajancent graph
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if pow((nums[i] + nums[j]), 1/2) == int(pow((nums[i] + nums[j]), 1/2)):
                    graph[i].append(j)

        # dfs iterate
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.visited[i] = 1
            self._dfs(i, 1, nums, graph)
            self.visited[i] = 0

        return self.res

    def _dfs(self, cur, cnt, nums, graph):
        if cnt == len(nums):
            self.res += 1
            return 

        last = -1
        for i in graph[cur]:
            if self.visited[i] == 1:
                continue
            if nums[i] == last:
                continue

            self.visited[i] = 1
            last = nums[i]
            self._dfs(i, cnt+1, nums, graph)
            self.visited[i] = 0