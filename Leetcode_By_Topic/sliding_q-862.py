# [17,85,93,-45,-21], 150
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        min_len, cur_sum = len(A) + 1, 0

        # The deque stores the possible values of the start pointer
        # [index, cur_sum]
        queue = collections.deque([[0, 0]])

        for end, val in enumerate(A):
            cur_sum += val

            # cur_sum == end, queue[0][1] == start
            # shrink the window and add
    
            while queue and (cur_sum - queue[0][1]) >= K:
                min_len = min(min_len, end - queue.popleft()[0] + 1)

            # dealing with negative
            while queue and cur_sum <= queue[-1][1]:
                # pop out the index before the negative num 
                # because we will never use it. If adding the neg will satisfy
                # the condition, then the count will start from the current neg idx
                queue.pop()

            queue.append([end + 1, cur_sum])
        return min_len if (min_len != len(A) + 1) else -1