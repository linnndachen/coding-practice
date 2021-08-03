from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # take k cards in the beginning
        res = total = sum(cardPoints[:k])
        for i in range(k):
            # Discard card (k-i-1)th, take card (n-i-1)th
            total += cardPoints[n - i - 1] - cardPoints[k - i - 1]
            res = max(res, total)
        return res

    """
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # begin[i] is the number of points we can obtain if we pick i cards in the beginning
        begin = [0] * (k + 1)
        # end[i] is the number of points we can obtain if we pick i cards in the end
        end = [0] * (k + 1)
        for i in range(k):#1
            begin[i + 1] = begin[i] + cardPoints[i]
            end[i + 1] = end[i] + cardPoints[n - i - 1]

        ans = 0
        for i in range(k + 1):
            ans = max(ans, begin[i] + end[k - i])
        return ans
    """