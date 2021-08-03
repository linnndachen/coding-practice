class Solution:
    """
    def decodeString(self, s: str) -> str:
        curString, stack, curK = "", [], 1

        for char in s:
            if char == "]":
                tmpt_s = []
                while stack[-1] != "[":
                    tmpt_s.append(stack.pop())
                # pop "["
                stack.pop()

                while stack and stack[-1].isdigit():
                    curK = curK*10 + int(stack.pop())
                curK = int(num[::-1]) if num else curK
                tmpt_s = "".join(tmpt_s)
                stack.append(tmpt_s * curK)

            else:
                stack.append(char)

        res = "".join(stack[::-1])

        return res[::-1]
    """

    def decodeString(self, s: str) -> str:
        curString, stack = "", []
        curNum = 0
        for char in s:
            if char == "[":
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif char == "]":
                num = stack.pop()
                preString = stack.pop()
                curString = preString + num * curString
            elif char.isdigit():
                curNum = curNum*10 + int(char)
            else:
                curString += char

        return curString