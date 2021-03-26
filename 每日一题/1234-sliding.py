from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        res, n = len(s), len(s)
        start = 0
        for end, char in enumerate(s):
            #print(count)
            count[char] -= 1
            #print(count)
            #print(all(n // 4 >= count[c] for c in 'QWER' ))
            while start < n and all(n // 4 >= count[c] for c in 'QWER' ):
                res = min(res, end - start + 1)
                count[s[start]] += 1
                start += 1

        return res