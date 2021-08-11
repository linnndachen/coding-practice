class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = 0
        res = 1
        for char in croakOfFrogs:
            if char == "c":
                c += 1

            elif char == "r":
                c -= 1
                if c < 0:
                    return -1

                r += 1

            elif char == "o":
                r -= 1
                if r < 0:
                    return -1
                o += 1

            elif char == "a":
                o -= 1
                if o < 0:
                    return -1
                a += 1

            elif char == "k":
                a -= 1
                if a < 0:
                    return -1

            res = max(res, c+r+o+a)

        if any([c, r, o, a]) > 0:
            return -1

        return res