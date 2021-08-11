class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        remove = set()
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(idx)
        for n in stack:
            remove.add(n)

        res = []
        for idx, char in  enumerate(s):
            if idx in remove:
                continue

            res.append(char)

        return "".join(res)