class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # replaced it with the question:
        # return subarray with K or less distinct num
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        """
        about res += window len: 
        we could do 1 + 2 + 3 + 4 (or length of [1] + length of [1,2] + 
        length of [1,2,1] + length of [1,2,1,2]).
        """
        count = collections.Counter()
        res, start = 0, 0

        for end in range(len(A)):
            # if this was a new num
            if count[A[end]] == 0:
                # I will use one distinc num
                K -= 1
            count[A[end]] += 1

            # when we don't have enough distinct num
            while K < 0:
                count[A[start]] -= 1
                if count[A[start]] == 0:
                    # free a quota
                    K += 1
                # shrink window until a quota is freed
                start += 1

            res += end - start + 1
        return res