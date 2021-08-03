class Solution:
    # knapsck dp 
    # normally we only need to consider the weights
    # here, we have 2 things to consider: the sub_sum and the sub_nums
    def splitArraySameAverage(self, A: List[int]) -> bool:
        A.sort()
        #DP[i] stores: how many nums can make up the sum - dp[i]
        # for example, if we have dp[i] = set(1, 4, 6) - we can use one numbers or 4 diff nums etc
        DP =[set() for _ in range(len(A)//2+1)]
        all_sum=sum(A)
        DP[0]=set([0])
        for item in A:
            for count in range(len(DP)-2,-1,-1):
                # if DP[i] is not empty
                if len(DP[count])>0:
                    # then update DP[i+1] by adding the current item into all sums in DP[i]
                    for a in DP[count]:
                        DP[count+1].add(a+item)
        
        for size in range(1,len(DP)):
            if all_sum*size/len(A) in DP[size]:
                return True
        return False
    """
    # backtrakcing
    # global avg: sum(nums) / len(nums) should equal to sum(group1) / len(group1)
    # same for group 2
    # global_sum/global_len = group_sum/group_len -> big_sum*small_len = small_sum*big_len
    def splitArraySameAverage(self, A: List[int]) -> bool:    
        self.total = sum(A)
        self.N = len(A)
        self.memo = {}

        for n1 in range(1, self.N // 2 + 1):
            if self.total * n1 % self.N == 0:
                if self.dfs(A, n1, self.total * n1 / self.N, 0):
                    return True
        return False

    def dfs(self, nums, n1, sum1, idx):
        if (n1, sum1, idx) in self.memo:
            return self.memo[(n1, sum1, idx)]

        if n1 == 0 and sum1 == 0:
            return True

        if idx == len(nums):
            return False

        # were not able to split
        if n1 == 0 or sum1 == 0:
            return False

        # pick this number and if it is True
        if self.dfs(nums, n1 - 1, sum1 - nums[idx], idx + 1):
            # it might works
            self.memo[(n1, sum1, idx)] = True
            return self.memo[(n1, sum1, idx)]

        # if we have duplicates numbers
        i = idx
        while i < len(nums) and nums[i] == nums[idx]:
            i += 1

        # if we don't pick this num
        if self.dfs(nums, n1, sum1, i):
            self.memo[(n1, sum1, i)] = True
            return True

        # if none of these satisfies
        self.memo[(n1, sum1, idx)] = False
        
        return self.memo[(n1, sum1, idx)]
    """