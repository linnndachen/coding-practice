class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = collections.Counter()
        start, k = 0, 2
        max_len = 0

        for end, char in enumerate(s):
            if d[char] == 0:
                k -= 1
            d[char] += 1

            while k < 0:
                d[s[start]] -= 1
                
                if d[s[start]] == 0:
                    k += 1
                
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len