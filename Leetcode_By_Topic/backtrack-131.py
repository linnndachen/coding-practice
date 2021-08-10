class Solution:
    def partition(self, s: str):
        """
        Relationship: continue to test each partition posibility until found a palidrome, 
        then add it to path, and continue to check the rest of the string.
        """
        res = []
        n = len(s)
        
        def dfs(path, i):
            # base case
            if i == n:
                res.append(path)
                return
            
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    dfs(path + [s[i:j+1]], j + 1)
        
        dfs([], 0)
        
        return res

test = Solution()
print(test.partition(s="aab"))