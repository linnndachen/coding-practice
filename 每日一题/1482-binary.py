class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # m groups with k elements in each group (also need to be ajacent)
        # bloomDay = [1,10,3,10,2] 
        # -> idx0 flower will bloom on day 1
        # -> idx4 flower will bloom on day 2
        # -> idx2 flower will bloom on day 3

        if len(bloomDay) < m*k:
            return -1

        left, right = 1, max(bloomDay)

        # Binary Search Template 2
        while left < right:
            mid = (left + right) // 2
            flower = bouq = 0

            # scan the array to count how many ajacents
            for d in bloomDay:
                flower = 0 if d > mid else flower + 1
                
                if flower >= k:
                    flower = 0
                    bouq += 1
                    
                    if bouq == m:
                        break

            if bouq == m:
                right = mid
            else:
                left = mid + 1

        return right