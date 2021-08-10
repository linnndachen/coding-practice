class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False

            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit



class Solution1:
    def isNumber(self, s: str) -> bool:
        # key: 找出指数 e
        # step 1: 清楚空格
        while s and s[0] == " ":
            s = s[1:]

        while s and s[-1] == " ":
            s = s[:-1]

        if not s:
            return False
        if len(s) == 1:
            return s[0].isdigit()

        # step 2: count e
        cnt, posE = 0, 0
        for idx, char in enumerate(s):
            if char in "eE":
                cnt += 1
                posE = idx

        if cnt > 1:
            return False

        if cnt == 1 and (s[0] in "eE" or s[-1] in "eE"):
            return False

        if cnt == 0:
            return self.isValid(s, 1)

        return self.isValid(s[:posE], 1) and self.isValid(s[posE+1:], 0)

    def isValid(self, s, k):
        # k represents decimal
        for idx, char in enumerate(s):
            if char in "+-" and idx != 0:
                return False

        if s[0] in "+-":
            s = s[1:]

        if not s or s == ".":
            return False

        cntDot = 0
        for idx, char in enumerate(s):
            if char == ".":
                cntDot += 1
            elif not char.isdigit():
                return False

        return cntDot <= k