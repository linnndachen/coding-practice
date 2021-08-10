class Solution:
    """
    def scoreOfParentheses(self, s: str) -> int:
        # "( ()(()) )"
        # 2 * "1+2" = 2*1 + 2*2
        stack = [0]

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                if stack:
                    v = stack.pop()
                    stack[-1] += max(2*v, 1)

        return stack.pop()
    """

    def scoreOfParentheses(self, S):
        res = left = 0
        for i, s in enumerate(S):
            if s == "(":
                left += 1
            else:
                left -= 1
                if S[i-1] == '(':
                    res += 2 ** left
        return res