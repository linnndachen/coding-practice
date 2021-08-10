class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        # divide into k+1 pieces
        # maximize the minimum sweetness


        # range of sweetness
        l, r = min(sweetness), sum(sweetness) // (K + 1)

        while l < r:
            mid = (l + r + 1) // 2

            cur_x, pieces = 0, 0

            for x in sweetness:
                cur_x += x

                if cur_x >= mid:
                    cur_x = 0
                    pieces += 1

                    if pieces > K + 1:
                        break

            if pieces >= K + 1:
                l = mid
            else:
                r = mid - 1
        return l