class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        """
        memo = {}
        return self.solve(piles, 0, len(piles)-1, memo)


    def solve(self, piles, i, j, memo):
        if i == j:
            return piles[i]

        if (i, j) in memo:
            return memo[(i, j)]

        memo[(i, j)] = max(piles[j]-self.solve(piles, i, j-1, memo), \
                           piles[i]-self.solve(piles, i+1, j, memo))

        return memo[(i, j)]
        """