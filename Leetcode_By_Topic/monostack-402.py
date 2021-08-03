class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        # becareful! the logic here is different
        # "112"
        # int(val) <= stack[-1]:
        # stack[-1] > int(val)
        for val in num:
            while stack and k and stack[-1] > int(val):
                stack.pop()
                k -= 1
            stack.append(int(val))

        # if k > 0
        finalStack = stack[:-k] if k else stack

        res = ""
        # get ride of front zeros
        for val in finalStack:
            if res == "" and val == 0:
                continue
            res += str(val)

        return res if res != "" else "0"