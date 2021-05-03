class Solution:
    def expand(self, s: str) -> List[str]:
        stack = ['']
        i = 0
        while i < len(s):
            if s[i].isalpha():
                stack = [k + s[i] for k in stack]
                i += 1
            else:
                candy = []
                while s[i] != "}":
                    if s[i].isalpha():
                        candy.append(s[i])
                    i += 1
                i += 1
                stack = [k + j for k in stack for j in sorted(candy)]
        return stack