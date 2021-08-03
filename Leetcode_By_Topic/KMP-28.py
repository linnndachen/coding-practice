class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        KMP logic:
        dp[i]: max len k such that p[0:k-1] = s[i-k+1:i]
        s: target string (haystack)
        p: targeted string (needle)
        s[i] 为结尾的后缀字符串 = p的前缀字符串
        当s某处的dp[i] 正好等于 len(p)， 那么就是matched
        """
        n, m = len(haystack), len(needle)

        # corner cases
        if m == 0:
            return 0

        if n == 0:
            return -1

        # No.1392
        suffix = self.preProcess(needle)
        
        dp = [0 for _ in range(n)]
        dp[0] = haystack[0] == needle[0]

        if m == 1 and dp[0] == 1:
            return 0

        for i in range(1, n):
            j = dp[i-1]

            # key difference between #1329 and this Q
            while j > 0 and haystack[i] != needle[j]:
                j = suffix[j-1]

            dp[i] = j + (haystack[i] == needle[j])

            if dp[i] == m:
                return i - m + 1

        return -1
    
    def preProcess(self, s):
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 0

        # 求后缀数组的5行代码
        for i in range(1, n):
            j = dp[i-1]

            while j >= 1 and s[j] != s[i]:
                j = dp[j-1]
            
            dp[i] = j+ (s[j] == s[i])

        k = dp[n-1]

        return dp

    """
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i

        return -1
    """