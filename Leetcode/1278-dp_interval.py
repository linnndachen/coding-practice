class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        n = len(s)
        memo = {}

        # calculate the cost of transferring one substring 
        # into palindrome string
        def cost(s,i,j):
            res = 0
            while i < j:
                if s[i] != s[j]:
                    res += 1
                i += 1
                j -= 1
            return res

        def dfs(idx, k):
            if (idx, k) in memo: 
                return memo[(idx, k)] #case already in memo

            #base case that each substring just have one character
            if n - idx == k:
                return 0

            #base case that need to transfer whole substring into palidrome
            if k == 1:
                return cost(s, idx, n - 1)

            res = float('inf')
            # keep making next part of substring into palidrome
            # here is "+2" because only 1 char has no cost, it has at least 2
            for j in range(idx + 1, n - k + 2):
                # cost of transfering i-j string + rest of the palidrome
                res = min(res, cost(s, idx, j - 1) + dfs(j, k - 1))
            memo[(idx, k)] = res
            return res
        return dfs(0 , k)