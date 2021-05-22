class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*":
            return True

        memo = {}

        # i is the length of s and j is the length of p
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    res = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], "."}
                    if j+1 < len(p) and p[j+1] == "*":
                        # we eliminate the current char
                        # or abcdd vs abcd* (last char matched,
                        # we can replicate the last char)
                        res = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        res = first_match and dp(i+1, j+1)

                memo[i, j] = res

            return memo[i, j]

        return dp(0, 0)
