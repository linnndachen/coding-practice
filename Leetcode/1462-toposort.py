# whether queries[i][0] is prerequisite of queries[i][1]
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        if len(prerequisites) == 0:
            return [False] * len(queries)

        graph = collections.defaultdict(list)
        degree = [0] * n
        pres = [set() for _ in range(n)]
        for parent, child in prerequisites:
            graph[parent].append(child)
            degree[child] += 1
            pres[child].add(parent)

        queue = collections.deque()
        for course, d in enumerate(degree):
            if d == 0:
                queue.append(course)

        while queue:
            parent = queue.popleft()
            for child in graph[parent]:
                pres[child] |= pres[parent]
                degree[child] -= 1
                if degree[child] == 0:
                    queue.append(child)

        return [pre in pres[course] for pre, course in queries]