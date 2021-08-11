class Solution:
    def calculate(self, s: str) -> int:
        stack, sign, num = [], '+', 0
        for i, char in enumerate(s + '+'):
            if char.isdigit():
                num = num*10 + int(char)
            # additional start#
            elif char == '(':
                stack.append(sign)
                stack.append('(')
                sign = '+'
            # additional end # 
            elif char in '+-*/)':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                # additional start#
                if char == ')':
                    num, item = 0, stack.pop()
                    while item != '(':
                        num += item
                        item = stack.pop()
                    sign = stack.pop()
                else:
                    sign, num = char, 0
        return sum(stack)

    """
    # recursive
    def calculate(self, s):
        s = s + "$"
        def helper(stack, i):
            num = 0
            sign = '+'
            while i < len(s):
                char = s[i]
                if char.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                elif char == '(':
                    num, i = helper([], i+1)
                else:
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack.append(stack.pop() * num)
                    if sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    i += 1
                    
                    if char == ')':
                        # sum the bracket stack, return ")" idx
                        return sum(stack), i
                    
                    sign = char 
            return sum(stack)
        return helper([], 0)
        """

"""
思路：
cal 1 - use stack to record the bracket sum
cal 2 - use stack to record each step's num, if */, we pop the num first, do cal
        at the end, we sum the step
cal 3 - we need to use 2 stacks (combo of the prev approach), each for cal1's and cal2's
        purpose. We can either do it recursivly or iterativly. Recursivly, we start a
        new stack == call the function when we meet "(". Iterativly, 
        
# clarify rules - to find out the variables that we need to mention
# walk through an example to see the logic - what would happen when we meet "(+_*/)"
"""