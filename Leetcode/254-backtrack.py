class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n < 2:
            return []

        res = []

        def dfs(i, curPath):
            num = curPath.pop()
            
            while i * i <= num:
                div = num // i
                if num % i == 0:
                    res.append(curPath + [i, div])
                    dfs(i, curPath+[i, div])

                i += 1
        dfs(2, [n])
        
        return res