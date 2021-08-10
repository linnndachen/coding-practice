class Solution:
    def minInsertions(self, s: str) -> int:
        # "()))()"
        res, right = 0, 0

        for char in s:
            if char == "(":
                if right % 2:
                    right -= 1
                    res += 1
                right += 2

            elif char == ")":
                right -= 1
                if right < 0:
                    right += 2
                    res += 1

        return right + res