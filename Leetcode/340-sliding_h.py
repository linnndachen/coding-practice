class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = collections.Counter()
        res, start = 0, 0

        for end, char in enumerate(s):
            if d[char] == 0:
                k -= 1
            d[char] += 1
            
            while k < 0:
                d[s[start]] -= 1
                
                if d[s[start]] == 0:
                    k += 1
                start += 1

            res = max(res, end - start + 1)

        return res