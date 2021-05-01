class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        tmpt = 0

        for _, char in enumerate(s):
            if char.isdigit():
                tmpt = 10*tmpt + int(char)

            elif char in "+-":
                res += tmpt * sign
                sign = 1 if char == "+" else -1
                tmpt = 0

            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            elif char == ")":
                res += tmpt * sign
                res *= stack.pop()
                res += stack.pop()
                tmpt = 0

        return res + tmpt * sign