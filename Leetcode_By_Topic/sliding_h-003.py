class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, start = 0, 0
        seen = set()

        for end, num in enumerate(s):
            while num in seen:
                seen.remove(s[start])
                start += 1

            seen.add(num)
            max_len = max(max_len, end - start + 1)

        return max_len