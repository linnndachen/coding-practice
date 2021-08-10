class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # we prioritize the tasks that give us most energy leftover
        # so that we could use those energy in further tasks.
        tasks.sort(key = lambda x: (x[0]- x[1]))
        curr = total = 0
        for a, m in tasks:
            if curr < m:
                total += m - curr
                curr = m
            curr -= a

        return total