class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, res = [], ""

        for s in path.split('/'):
            if s not in "..":
                stack.append(s)
            if s == ".." and stack:
                stack.pop()

        for char in stack:
            res = res + "/" + char

        return res if res != "" else "/"