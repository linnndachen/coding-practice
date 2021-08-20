class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pToS = {}
        sToP = {}

        def dfs(i, j):
            if i == len(pattern) and j == len(s):
                return True

            if i == len(pattern) or j == len(s):
                return False

            char = pattern[i]
            if char in pToS:
                curStr = pToS[char]
                k = len(curStr)
                if k + j > len(s):
                    return False

                if s[j:j+k] != curStr:
                    return False

                return dfs(i+1, j+k)
            else:
                for k in range(j, len(s)):
                    # note: 在 d 的长度这里debug了很久
                    d = k-j+1
                    curStr = s[j:j+d]
                    if curStr in sToP:
                        continue

                    pToS[char] = curStr
                    sToP[curStr] = char

                    if dfs(i+1, j+d):
                        return True

                    del pToS[char]
                    del sToP[curStr]

                return False

        return dfs(0, 0)
