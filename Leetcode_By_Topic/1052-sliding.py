class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied, unsatisfied, trickSatisfied = 0, 0, 0

        for end, customer in enumerate(customers):
            if grumpy[end] == 0:
                satisfied += customer
            else:
                unsatisfied += customer

            if end >= X:
                # remove unsatisfied customer from left end of the window
                unsatisfied -= customers[end - X] * grumpy[end - X]
            
            trickSatisfied = max(trickSatisfied, unsatisfied)

        return satisfied + trickSatisfied