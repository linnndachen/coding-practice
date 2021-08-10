class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        c = collections.Counter({0: 1}) # [1,0,1,0,1] #[0, 1, 1, 2, 2, 3]
        psum = res = 0
        for n in A:
            psum += n
            res += c[psum - S]
            c[psum] += 1

        return res

        """"
        def numSubarraysWithSum(self, A: List[int], S: int) -> int:
            # if current ones bigger than S, shorten the window
            def atMost(target):
                start, count = 0, 0

                for end, num in enumerate(A):
                    target -= num
                    while target < 0 and start <= end:
                        target += A[start]
                        start += 1
                    count += end - start + 1
                return count

            return atMost(S) - atMost(S - 1)
        """

        """
        # sliding window
        start = cur_sum = 0
        count, res = 0, 0
        for end, num in enumerate(A):
            cur_sum += num

            # reset count to 0 and try to increase the left pointer.
            # if the cur_sum is not S yet, it wouldn't affect anything
            # if the cur_sum is equal to S, cur_sum must change and we need recount
            if num == 1:
                count = 0

            while start <= end and cur_sum >= S:
                if cur_sum == S:
                    count += 1

                cur_sum -= A[start]
                start += 1
            res += count

        return res
        """