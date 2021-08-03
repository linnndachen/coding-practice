# check there exist a seq
# check that's the only seq
# check the only seq is the same as the given one
from collections import deque
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = {}
        degree = {}
        for seq in seqs:
            for num in seq:
                degree[num] = 0
                graph[num] = []

        # stop early
        if len(degree) != len(org):
            return False

        for seq in seqs:
            for i in range(len(seq) - 1):
                parent = seq[i]
                child = seq[i + 1]
                graph[parent].append(child)
                degree[child] += 1


        sources = deque()
        for key in degree:
            if degree[key] == 0:
                sources.append(key)

        res = []

        while sources:
            if len(sources) > 1:
                return False

            parent = sources.popleft()
            res.append(parent)
            
            for child in graph[parent]:
                degree[child] -= 1
                if degree[child] == 0:
                    sources.append(child)

        return res == org