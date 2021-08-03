from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {c: i for i, c in reversed(list(enumerate(s)))}
        last = {c: i for i, c in enumerate(s)}

        res, prev = [], -1
        # 越早结束越好
        for i in sorted(last.values()):
            start, end = first[s[i]], last[s[i]]
            j = end

            # make sure the end is the same, else invalid
            while j >= start and end > prev and end == i:
                start = min(start, first[s[j]])
                end = max(end, last[s[j]])
                j -= 1
            if end == i and start > prev:
                res.append(s[start:end+1])
                prev = end

        return res