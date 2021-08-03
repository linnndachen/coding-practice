class Solution:
    def longestAwesome(self, s: str) -> int:
        # the difference betweent this question and 1371 is we need to consider case 2
        def _count2key(arr):
            key = 0
            for i in range(10):
                # 把频次的奇偶性左移i位，变成bit
                key += ((count[i] % 2) << i)
            return key

        count = [0] * 10
        # hashmap - 对于某个数字，它的前缀是odd or even
        memo = {0: -1}
        res = 0
        for j, val in enumerate(s):
            count[int(s[j])] += 1

            key = _count2key(count)
            # case 1
            if key in memo:
                res = max(res, j - memo[key])
            else:
                memo[key] = j

            # case 2
            for k in range(10):
                newkey = key
                # flipping
                if (((newkey >> k)&1) == 0):
                    newkey  += (1 << k)
                else:
                    newkey  -= (1 << k)
                    
                if newkey in memo:
                    res = max(res, j - memo[newkey])

        return res

        """
        res, cur, n = 0, 0, len(s)
        seen = [-1] + [n] * 1024
        for i, c in enumerate(s):
            cur ^= 1 << int(c)
            for a in range(10):
                res = max(res, i - seen[cur ^ (1 << a)])
            res = max(res, i - seen[cur])
            seen[cur] = min(seen[cur], i)
        return res
        """