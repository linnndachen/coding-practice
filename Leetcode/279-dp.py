class Solution:

    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float("inf")] * (n+1)

        # bottom up base case
        dp[0] = 0

        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)

        return dp[-1]


    """
    # top down - if with cache
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]

        def helper(n):
            if n in square_nums:
                return 1

            min_num = float("inf")

            for square in square_nums:
                if n < square:
                    break

                new_n = helper(k-n) + 1
                min_num = min(new_n, min_num)
            return min_num

        return helper(n)


    # wrong code
    def numSquares(self, n: int) -> int:
        self.memo = {}
        self.memo[0] = 0
        
        def helper(num):
            # wrong 1: base case
            # if num is valid should be our base case
            # we can directly return
            if num == 0:
                return 0
            
            square = math.sqrt(num)
            if square == int(square):
                self.memo[num] = min(1 + self.memo.get(n-num, 0), n//num)

            else:
                self.memo[num] = 0
                
            helper(num-1)
            # print(self.memo, num)
            return self.memo[num]
        
        return helper(0)
    """