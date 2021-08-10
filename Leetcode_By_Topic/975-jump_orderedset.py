class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_min_higher, next_max_lower = [0] * n, [0] * n

        stack = []
        # iterating from small to big
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            # index smaller than i and value bigger than i
            while stack and stack[-1] < i:
                # the idx with minimum larger value than i
                next_min_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                next_max_lower[stack.pop()] = i
            stack.append(i)

        even, odd = [0] * n, [0] * n

        even[-1] = odd[-1] = 1
        for i in range(n-2, -1, -1):
            odd[i] = even[next_min_higher[i]]
            even[i] = odd[next_max_lower[i]]

        # starting idx has to make an odd jump - higher jump
        return sum(odd)