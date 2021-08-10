class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = "+"
        tmpt = 0

        for idx, char in enumerate(s):
            if char.isdigit():
                tmpt = 10*tmpt + int(char)
    
            if char in "+-*/" or idx == len(s) - 1:
                if sign == "+":
                    stack.append(tmpt)
                elif sign == "-":
                    stack.append(-tmpt)
                elif sign == "*":
                    stack.append(stack.pop()*tmpt)
                else:         
                    stack.append(int(stack.pop()/tmpt))

                tmpt = 0
                sign = char
        return sum(stack)