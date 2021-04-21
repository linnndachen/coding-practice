class Solution:    
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}
        suffix_sum = [0] * n
        for i in range(n):
            suffix_sum[i] = sum(piles[i:])
        
        return self.minimax(piles, memo, suffix_sum, 0, 1)
    
    
    def minimax(self, piles, memo, suffix_sum, idx, M):
        """
        这个function是用来算，每一个我在的idx, 对手所有可以走的range中，拿个最小
        （minimized），然后总数-对手，就是我能拿到最大的
        """
        if idx >= len(piles):
            return 0

        if (idx, M) in memo:
            return memo[(idx, M)]

        # if what the opponent can take is > what's left
        if len(piles) - idx <= 2 * M:
            return suffix_sum[idx]

        minimized = float('inf')
        for X in range(1, 2 * M + 1): # range of pile
            # minimized opponent's move
            minimized = min(minimized, self.minimax(piles, memo, suffix_sum, idx+X, max(M, X)))
        memo[(idx, M)] = suffix_sum[idx] - minimized

        return memo[(idx, M)]

# 1: x = 1 [1, 2M]
# 2: M = 1, [1, 2], X = 2
# 3: M = max(1, 2), [1, 4], X = 1
# 4: M = max(2, 1), [1, 4]