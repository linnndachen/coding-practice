class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtrack(candidates, target, res, [], 0)
        return res
    
    def backtrack(self, candidates, target, res, path, idx):
        if target == 0:
            res.append(path[:])
            return 
        
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                break
            
            path.append(candidates[i])
            self.backtrack(candidates, target-candidates[i], res, path, i)
            path.pop()
