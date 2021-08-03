class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [1] * (n+1)
        stack = []

        for i , a in enumerate(arr + [float('inf')]):
            while stack and arr[stack[-1]] < a:
                lower = [stack.pop()]

                # get all the duplicates
                while stack and arr[stack[-1]] == arr[lower[0]]:
                    lower.append(stack.pop())

                # for all the same values that satisfy arr[i] > arr[j]
                for j in lower:
                    if abs(i - j) <= d:
                        dp[i] = max(dp[i], dp[j]+1)
                    # arr[stack[-1]] is bigger than arr[j] and smaller than arr[stack[-2]]
                    # if we update arr[j], we also update arr[stack[-1]]
                    # because stack[-1] can also jump to j
                    if stack and j - stack[-1] <= d:
                        print(stack, j, i)
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j]+1)
            stack.append(i)

        return max(dp[:-1])

    """
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n

        def dfs(i):
            if dp[i]:
                return dp[i]
            dp[i] = 1
            for di in [-1, 1]:
                for j in range(i+di, i+(di*d)+di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    dp[i] = max(dp[i], dfs(j) + 1)

            return dp[i]

        for i in range(n):
            dfs(i)

        return max(dp)
    """

    """
    def maxJumps(self, arr: List[int], d: int) -> int:
        n= len(arr)
        # stores how many idx we can visit if we start from i idx
        dp = [1]* n

        lst = sorted([(a,i) for i, a in enumerate(arr)])

        for a, i in lst:
            # search to the right
            for j in range(i+1, min(i+d+1, n)):
                if arr[j] >= a:
                    break
                else:
                    dp[i] = max(dp[i], dp[j] + 1)
            # search to the left        
            for k in range(i-1, max(-1, i-d-1), -1):
                if arr[k] >= a:
                    break
                else:
                    dp[i] = max(dp[i], dp[k] + 1)

        return max(dp)
    """