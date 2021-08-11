class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res, start = 0, 0
        counter = collections.defaultdict(int)

        for end, char in enumerate(s):
            counter[char] += 1

            while len(counter) == 3:
                res += len(s) - end # which is start

                # shrink the window
                counter[s[start]] -= 1
                if not counter[s[start]]:
                    del counter[s[start]]
                start += 1
        return res