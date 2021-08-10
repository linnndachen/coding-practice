class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # when window > total current ones + K, we need to shorten it

        start, cur_ones = 0, 0
        res = 0

        for end, val in enumerate(A):
            if val == 1:
                cur_ones += 1
            
            while end - start + 1 - cur_ones > K:
                if A[start] == 1:
                    cur_ones -= 1 
                start += 1

            res = max(res, end - start + 1)

        return res