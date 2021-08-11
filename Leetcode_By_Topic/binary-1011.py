class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # ship all the weights within D days

        # max: ship everything in a day
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2

            cur_weight, days = 0, 1
            for w in weights:
                # Note: I missed the "w + cur" detail here
                if w + cur_weight > mid:
                    cur_weight = 0
                    days += 1
                    
                    if days > D:
                        break

                cur_weight += w

            # need to increae mini weight
            if days > D:
                l = mid + 1
            else:
                r = mid

        return r