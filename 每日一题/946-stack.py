class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # push everything to the stack until it equals to the first one to pop
        # pop as long as they are the same element
        j = 0 # pop index
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)