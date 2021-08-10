class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 1 - each group == -1 item is in its own group 
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = m
                m += 1

        # 2 - build graph
        items_graph = [[] for _ in range(n)]
        indegree_items = [0] * n
        
        groups_graph = [[] for _ in range(m)]
        indegree_groups = [0] * m        

        for item in range(n):
            for parent in beforeItems[item]:
                # graph within each group
                items_graph[parent].append(item)
                indegree_items[item] += 1
                
                # if not in the same group
                if group[item] != group[parent]:
                    # record this in the group graph
                    groups_graph[group[parent]].append(group[item])
                    indegree_groups[group[item]] += 1

        # 3 - Find topological orders of items and groups.
        item_order = self.topo_sort(items_graph, indegree_items)
        group_order = self.topo_sort(groups_graph, indegree_groups)
        
        if not item_order or not group_order:
            return []

        # 4 - Find order of items within each group.
        order_within_group = collections.defaultdict(list)
        for item in item_order:
            order_within_group[group[item]].append(item)

        # 5 - Combine ordered groups.
        res = []
        for group in group_order:
            res += order_within_group[group]
        return res

    def topo_sort(self, graph, degree):
        queue= collections.deque()
        for item in range(len(degree)):
            if degree[item] == 0:
                queue.append(item)

        res = []
        while queue:
            item = queue.popleft()
            res.append(item)
            
            for child in graph[item]:
                degree[child] -= 1
                if degree[child] == 0:
                    queue.append(child)

        return res if len(res) == len(degree) else []