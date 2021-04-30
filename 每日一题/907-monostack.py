class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        """
        example: [3,2,1,5,6,0,9,7]
        # assume i == 1
        # nothing before 1 is smaller than 1, so it would be until 3 (boundary)
        # it is not until 0, where we meet a number smaller than 1
        
        why do we need to find the smallest? because instead of finding every combination,
        we find the smallest num and find all of its combinations. The reasons is, it can combine
        with the most elements and be the smallest one
        then we find the second smallest one and repeat the step (excluding the smallest set)
        
        Edge Cases: duplicates 2 [3 5 5 5 3 5 5 3] 2
        In this case, we might be counting the same subarry 3 times
        - To solve this, in Prev section, we used <= 
        - in the Post section, we used < only we avoid duplicating array
        """
        MOD = 10**9 + 7
        N = len(A)

        # prev has i* - 1 in increasing order of A[i* - 1]
        stack = []
        prev = [None] * N
        for i in range(N):
            # stops, when we find the next smallest element/boundary
            # 新来的num <= 前面的数
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()

            # record boundary or the cloest number smaller than i in nums[:i]
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        next_ = [None] * N
        for k in range(N-1, -1, -1):
            # 新来的num < 后面的数，说明没有大于的
            while stack and A[k] < A[stack[-1]]:
                stack.pop()

            # find boundary or the next one that's smaller than i
            next_[k] = stack[-1] if stack else N
            stack.append(k)

        # all combos with A[i] as the smallest element * A[I]
        return sum((i - prev[i]) * (next_[i] - i) * A[i]
                   for i in range(N)) % MOD

    def onePass(self, A):
        res = 0
        s = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10**9 + 7)

    """
    If A[j] <= A[i] (j<i), result[i] = result[i-1] + A[i], then result[i] = result[j] + A[i]*(i-j)

    Example: Let's take i=4 and look at subarrays for the element A[i]=4:
    [3,1,2,5,4], [1,2,5,4], [2,5,4], [5,4], [4]

    First part of these subarrays look similar to subarrays generated previous less value 2 
    at j=2 as if we took those subarrays ([3,1,2], [1,2], [2]) and added elements [5,4] to 
    each of them. Sum of those subarrays equals result[j].

    The rest of our i-th subarrays consist of elements after j and up to i: [5,4], [4] . 
    They are not less then our element 4 so their sum equals to (i-j)*A[i]

    Together these two observations give us formula result[i] = result[j] + A[i]*(i-j)
    """