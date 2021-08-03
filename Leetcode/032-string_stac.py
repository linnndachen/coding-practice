class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        res = 0

        for char in s:
            if char == "(":
                stack.append(0) 
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val+2
                    res = max(res, stack[-1])
                else:
                    stack = [0]
        return res

    """
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    res = max(res, idx - stack[-1])

        return res
    """