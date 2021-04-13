class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def label_to_position(label):
            # divmod: (label - 1) // n, (label - 1) % n
            r, c = divmod(label-1, n)
            if r % 2 == 0:
                return n-1-r, c
            else: # reversed order
                return n-1-r, n-1-c

        seen = set()
        queue = collections.deque()
        queue.append((0, 1))
        while queue:
            step, label = queue.popleft()
            r, c = label_to_position(label)
            if board[r][c] != -1:
                label = board[r][c]
            if label == n*n:
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n*n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((step+1, new_label))
        return -1