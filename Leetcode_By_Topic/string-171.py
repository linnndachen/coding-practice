class Solution:
    """
    def titleToNumber(self, columnTitle: str) -> int:
        # 26 * 26 ^ len(char)-1
        res = 0

        alpha_map = {chr(i+65): i + 1 for i in range(26)}

        n = len(columnTitle) # 2
        for i in range(n):
            # note: 这里我们需要char 从后往前，但是i依然是从小到大
            cur_char = columnTitle[n-1-i]
            res += (alpha_map[cur_char] * (26**i))

        return res
    """

    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        n = len(columnTitle)

        for i in range(n):
            res *= 26
            res += (ord(columnTitle[i]) - ord("A") + 1)

        return res