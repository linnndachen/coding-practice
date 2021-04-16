class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtrack(k, n, res, [], 1)
        return res

    def backtrack(self, k, target, res, path, idx):
        if target == 0 and len(path) == k:
            res.append(path[:])
            return 

        for i in range(idx, 10):
            if i > target:
                break

            path.append(i)
            self.backtrack(k, target-i, res, path, i+1)
            path.pop()