class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or char != stack[-1][0]:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
                    
        return ''.join(c * k for c, k in stack)
    """
    # my logic but with some duplicate codes
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or char != stack[-1][0]:
                stack.append([char, 1])
            else:
                prev, count = stack[-1]
                new_count = count + 1
                stack.append([char, new_count])
                if new_count == k:
                    for _ in range(k):
                        stack.pop()

        return "".join([i[0] for i in stack])
    """

    """
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return None
        #Recursive
        size = len(s)
        count = 1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            elif s[i]!=s[i-1]:
                count = 1

            if count == k:
                #found duplicates to remove
                s=s.replace(s[i-k+1:i+1], "")

                #backpropogate returned string
                return self.removeDuplicates(s,k)

        return s
    """