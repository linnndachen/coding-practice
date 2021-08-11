class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        presum = [0] * (n)
        presum[0] = arr[0]

        for i in range(1, n):
            presum[i] = presum[i-1] + arr[i]

        # corner case
        if presum[-1] <= target:
            return arr[-1]

        def _checkSum(mid):
            idx = bisect_right(arr, mid)
            total = 0

            if (idx-1) >= 0:

                total += presum[idx-1]

            total += mid * (n - idx)

            return total


        left, right = 0, arr[-1]

        while left < right:
            mid = (left+right) // 2
            
            if _checkSum(mid) == target:
                return mid

            if _checkSum(mid) > target:
                right = mid
            else:
                left = mid+1

        sum1 = _checkSum(left)
        sum2 = _checkSum(left - 1)
        if abs(sum1 - target) < abs(sum2 - target):
            return left
        else:
            return left - 1


    """
    def findBestValue(self, arr: List[int], target: int) -> int:    
        arr.sort()
        presum, n = 0, len(arr)

        for i in range(n):
            res = round((target - presum)/n)
            if res <= arr[i]: 
                return res
            presum += arr[i]
            n -= 1

        return arr[-1]
    """