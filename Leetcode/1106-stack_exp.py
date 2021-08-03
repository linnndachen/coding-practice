class Solution:
    # specify the operators first - put them as function
    # stack directly append t, f
    # "(" enter the stack as normal, ")" exist stack and store all brackets in a sperate stack
    # after handling the full bracket, we put the sub-res back to the stack
    def parseBoolExpr(self, expression: str) -> bool:
        func = {'&' : all, '|' : any, '!' : lambda x : not x[0]}

        stack = []
        for c in expression:
            if c in func:
                stack.append(func[c])
            elif c == '(':
                stack.append('(')
            elif c == 'f':
                stack.append(False)
            elif c == 't':
                stack.append(True)

            elif c == ')':
                # store expressions within the bracket
                ss = []
                while stack[-1] != '(':
                    ss.append(stack.pop())
                # pop out the "("
                stack.pop()

                # stack.pop() will give us the operator
                # then we operator on the (ss) expressions
                # append to the result
                stack.append(stack.pop()(ss))

        return stack.pop()

"""
# recursion
class Solution:
    # t, f directly handle to res
    # [] for expression in the bracket
    # specify how to handle "| & !"
    def parseBoolExpr(self, expression: str) -> bool:
        def helper(i):
            # means we only have 1 char
            if expression[i] in ["t", "f"]:
                return True if expression[i] == "t" else False, i+1

            # else, i+1 must be "(". We start with i+2
            op = expression[i]
            i, stack = i+2, []

            while expression[i] != ')':
                if expression[i] == ',': 
                    i += 1
                    continue

                res, i = helper(i)
                stack.append(res)

            if op == '&':
                return all(stack), i+1
            elif op == '|':
                return any(stack), i+1
            elif op == '!':
                return not stack[0], i+1

        res, i = helper(0)
        return res
        """

"""
# cheating
def parseBoolExpr(self, expression: str) -> bool:
    # &, | and ! == all, any and not.
    return eval(expression.replace('f', 'False').replace('t', 'True').replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))
"""