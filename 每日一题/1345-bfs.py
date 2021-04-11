class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0

        same_val = collections.defaultdict(list)
        for idx, num in enumerate(arr):
            same_val[num].append(idx)

        queue = deque([(0, 0)])
        seen = set()

        while queue:
            steps, pos = queue.popleft()
            
            if pos == len(arr) - 1:
                return steps
            
            for i in [pos-1, pos + 1]:
                if 0 <= i < len(arr) and i not in seen:
                    queue.append((steps+1, i))
                    seen.add(i)

            if same_val[arr[pos]]:
                for nb in same_val[arr[pos]]:
                    if nb not in seen:
                        queue.append((steps+1, nb))
                        seen.add(nb)
                same_val[arr[pos]] = None
        return -1