class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, n = [], len(T)
        res = [0] * n

        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                pre_idx = stack.pop()
                res[pre_idx] = i - pre_idx
            stack.append(i)
        return res