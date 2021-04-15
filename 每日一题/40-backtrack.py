class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtrack(candidates, target, res, [], 0)
        return res

    def backtrack(self, candidates, target, res, path, idx):
        if target == 0:
            res.append(path[:])
            return 
        
        for i in range(idx, len(candidates)):            
            if i > idx and candidates[i] == candidates[i-1]:
                continue

            if candidates[i] > target:
                break

            path.append(candidates[i])
            self.backtrack(candidates, target-candidates[i], res, path, i+1)
            path.pop() 