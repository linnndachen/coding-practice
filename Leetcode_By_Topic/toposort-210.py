class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        graph = {i :[] for i in range(n)}
        degree = [0] * n

        for parent, child in prerequisites:
            graph[parent].append(child)
            degree[child] += 1

        res = [i for i in range(n) if degree[i] == 0]
        for parent in res:
            for children in graph[parent]:
                degree[children] -= 1
                
                if degree[children] == 0:
                    res.append(children)

        return res[::-1] if len(res) == numCourses else []