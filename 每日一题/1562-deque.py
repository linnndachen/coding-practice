class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return m

        arr.insert(0, 0)
        res, day = -1, {}

        # because it is 1 indexed
        for i in range(1, n + 1):
            # day{flip which idx: which day to flip}
            day[arr[i]] = i

        queue = collections.deque()
        for i in range(1, n + 1):
            # pop out the smaller values
            while queue and day[queue[-1]] < day[i]:
                queue.pop()

            # out of range
            while queue and i - queue[0] >= m:
                queue.popleft()

            queue.append(i)

            if i < m:
                continue
            maxi = day[queue[0]]
            
            # the left idx and right idx of the valid window
            left, right = float('inf'), float('inf')

            if i - m >= 1:
                left = day[i-m]
            if i + 1 <= n:
                right = day[i+1]
            # both days have to come after the window are all ones
            if maxi < left and maxi < right:
                res = max(res, min(left, right) - 1)

        return res