class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = [[""]]
        for c in expression:
            if c == "{":
                stack.append(c)
                stack.append([""])
            elif c == "}":
                # Union all values until "{"
                union_set = set()
                # print(stack)
                while stack[-1] != "{":
                    union_set |= set(stack.pop())

                stack.pop()  # pop the "{"
                product = [i + u for i in stack[-1] for u in union_set]
                stack[-1] = product
            
            # meaning it belongs to a set
            elif c == ",":
                stack.append([""])
            else: # char
                stack[-1] = [i + c for i in stack[-1]]

        return sorted(stack[-1])

    """
    # not optimizing the duplicate ones
    def braceExpansionII(self, expression: str) -> List[str]:
        stack,res,cur=[],[],[]
        for i in range(len(expression)):
            v=expression[i]
            if v.isalpha():
                cur=[c+v for c in cur or ['']]
            elif v=='{':
                stack.append(res)
                stack.append(cur)
                res,cur=[],[]
            elif v=='}':
                pre=stack.pop()
                preRes=stack.pop()
                cur=[p+c for c in res+cur for p in pre or ['']]
                res=preRes
            elif v==',':
                res+=cur
                cur=[]
        return sorted(set(res+cur))
    """
# Rules: {} represent a set - no duplicates
# if e{x,y} meaing ex, ey
# for 2 sets{} {}, each char needs to match the one in the other set
# "{{a,b},{b,c}}"