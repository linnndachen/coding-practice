from collections import Counter
from typing import List

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        cnt = Counter(s)
        odd_char = ""
        
        for char in cnt:
            if cnt[char] % 2 == 1:
                if odd_char:
                    return []
                else:
                    odd_char = char
                    cnt[char] -= 1

        def dfs(path):
            if len(path) == len(s) // 2:
                res.append("".join(path) + odd_char + "".join(path[::-1])) 
            
            for char in cnt:
                if cnt[char] > 0:
                    cnt[char] -= 2
                    dfs(path+[char])
                    cnt[char] += 2

        res = []
        dfs([])

        return res