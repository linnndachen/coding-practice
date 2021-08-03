class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] 
        s2 = float("-inf")
        for n in nums[::-1]:
            if n < s2:
                return True
            # decreasing stack, the biggest at the bottom, smallest on top
            while stack and stack[-1] < n:
                # n could be the biggest and s2 will be the second biggest
                s2 = stack.pop()
            stack.append(n)
        return False