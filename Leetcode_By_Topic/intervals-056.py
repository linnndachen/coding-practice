class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return
        
        res = []
        arr = sorted(intervals, key=lambda x: x[0]) #NlogN
        
        for pair in arr: #N
            # if first pair / don't overlap
            if not res or res[-1][1] < pair[0]:
                res.append(pair)
            else:
                # if overlap, merge
                res[-1][1] = max(res[-1][1], pair[1])
        
        return res