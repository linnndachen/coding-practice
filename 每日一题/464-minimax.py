class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        self.seen = {}
        max_sum = (maxChoosableInteger + 1) * maxChoosableInteger / 2
        if max_sum < desiredTotal:
            return False

        # if the sum matches desiredTotal exactly then you win if there's an odd number of turns
        if max_sum == desiredTotal:
            return maxChoosableInteger % 2

        choices = list(range(1, maxChoosableInteger + 1))
        return self.dfs(choices, desiredTotal)

    def dfs(self, choices, remainder):
        # if this is my turn and the biggest num can achieve the goal
        if choices[-1] >= remainder:
            return True

        seen_key = tuple(choices)
        if seen_key in self.seen:
            return self.seen[seen_key]

        # if we haven't won yet.. it's the next player's turn.
        for idx in range(len(choices)):
            # player2 cannot pick the choice I have picked
            # if player2 did not win the game 
            if not self.dfs(choices[:idx]+choices[idx+1:], remainder-choices[idx]):
                # then I could win
                self.seen[seen_key] = True
                # I return true if I found 1 path to win
                return True

        # if I have tried all possible combinations and I did not win
        self.seen[seen_key] = False
        # I lost
        return False