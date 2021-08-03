class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize
        # find the source nodes and add to queue
        # sort each source node: 
            # Add it to res
            # Get all of its children from the graph.
            # Decrement the in-degree of each child by 1.
            # If a child’s in-degree becomes ‘0’, add it to the sources Queue.
            # Repeat step 1, until the source Queue is empty.
        n = numCourses
        graph = {i: [] for i in range(n)}
        degree = [0] * n

        for parent, child in prerequisites:
            graph[parent].append(child)
            degree[child] += 1

        bfs = [i for i in range(n) if degree[i] == 0]
        for parent in bfs:
            for children in graph[parent]:
                degree[children] -= 1
                
                if degree[children] == 0:
                    bfs.append(children)
        return len(bfs) == n