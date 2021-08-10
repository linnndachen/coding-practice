class Solution:
    def countArrangement(self, n):
        @lru_cache(None)
        def dfs(bm, pos):
            if pos == 0:
                return 1
                
            count = 0
            for i in range(n):
                # if still empty + qualifies
                if not bm&1 << i and ((i+1) % pos == 0 or pos % (i+1) == 0):
                    count += dfs(bm^1 << i, pos - 1)
            return count
                
        return dfs(0, n)
"""    
class Solution:
    def countArrangement(self, n: int) -> int:
        used = [False] * (n+1)
        self.res = 0
        
        self.backtrack(n, used, 1)
        return self.res

    def backtrack(self, n, used, pos):
        if pos > n:
            self.res += 1
            return 
        
        for i in range(1, n+1):
            if used[i]:
                continue
            
            if i % pos == 0 or pos % i == 0:
                used[i] = True
                self.backtrack(n, used, pos+1)
                used[i] = False
    """