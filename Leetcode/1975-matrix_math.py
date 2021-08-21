from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # if we have even amount of negative, we can turn all of them to positive
        # if we have an odd amount, one number will has to stay negative
        # that will the smallest number
        maxSum, neg = 0, 0
        m, n = len(matrix), len(matrix[0])
        smallest = float('inf')

        for i in range(m):
            for j in range(n):
                maxSum += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    neg += 1

                smallest = min(smallest, abs(matrix[i][j]))
        return maxSum if neg%2 == 0 else maxSum - 2*smallest