class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # find the value of our starting index
        # we can + or -, if node already in seen, return false
        # if we are at arr[i] == 0, return True
        # use bfs to find the shortest path - reach there quicker 
        seen, queue = set(), collections.deque([start])

        while queue:
            idx = queue.popleft()
            
            if arr[idx] == 0:
                return True

            delta = arr[idx]

            for choice in idx + delta, idx - delta:
                if choice not in seen and 0 <= choice < len(arr):
                    queue.append(choice)
                    seen.add(choice)

        return False