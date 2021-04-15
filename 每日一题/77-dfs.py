class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(n, k,[], 1, res)
        return res

    def backtrack(self, n, k, path, idx, res):
        if len(path) == k:
            res.append(path[:])
            return 
        
        for num in range(idx, n+1):
            path.append(num)
            self.backtrack(n, k, path, num+1, res)
            path.pop()