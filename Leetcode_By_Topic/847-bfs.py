# difference from traditional bfs - nodes can be re-visit 
# So, the time and space will be 2^n
# we also need to record a "state" in the queue
# another thing is because we can start at any point, we will start with pushing
# all the nodes into the queue
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        masks = [1 << i for i in range(n)]
        states = [{masks[i]} for i in range(n)]
        # used to check whether all nodes have been visited (11111...111)
        target = (1 << n) - 1

        cur_queue = [(i, masks[i]) for i in range(n)]
        steps = 0


        while cur_queue:
            next_queue = []
            for cur_node, visited in cur_queue:
                if visited == target:
                    return steps
            
                # start bfs from each neighbor
                for nb in graph[cur_node]:
                    new_visited = visited | masks[nb]
                    if new_visited == target:
                        return steps + 1
                    if new_visited not in states[nb]:
                        states[nb].add(new_visited)
                        next_queue.append((nb, new_visited))

            cur_queue = next_queue
            steps += 1

        return inf