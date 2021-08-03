from collections import Counter, defaultdict
from typing import List

class Solution:
    # NOTE: 还不太懂这个solution
    def __init__(self):
        self.res = float("inf")
        
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        if any(cnt[num] > k for num in cnt):
            return -1

        bags = [[] for i in range(k)]
        n = len(nums)
        M = n // k
        nums.sort()

        # precalculate gaps_sum for pruning
        numbers = sorted(cnt.keys())
        gaps = defaultdict(int)

        for i in range(1,len(numbers)):
            gaps[numbers[i]] = numbers[i] - numbers[i-1]

        s, cur = 0, []
        gaps_sum = defaultdict(int)

        for i in range(n-1,-1,-1):
            bisect.bisect(cur, gaps[nums[i]])
            s += gaps[nums[i]]
            gaps_sum[i,0] = s

            for empty in range(1, min(k+1,len(cur))):
                gaps_sum[i, empty] = gaps_sum[i, empty-1] - cur[-empty]

        def _dfs(i, cur_res, empty_bags):
            # put #i number in #j bags
            if i == n:
                self.res = min(self.res,cur_res)
                return

            if cur_res + gaps_sum[i, empty_bags] >= self.res: 
                return 

            for j in range(k):
                # encounter same combination
                if (j > 0 and bags[j] == bags[j-1]):
                    continue

                # duplicate number in some bags
                elif (bags[j] and bags[j][-1] == nums[i]):
                    continue

                # bag is full
                elif (len(bags[j]) == M):
                    continue

                else:
                    bags[j].append(nums[i])
                    if len(bags[j]) == 1:
                        _dfs(i+1, cur_res, empty_bags-1)
                    else:
                        _dfs(i+1, cur_res+bags[j][-1]-bags[j][-2], empty_bags)
                    bags[j].pop()

        _dfs(0,0,k)
        return self.res
    

"""
# 原始答案 + 相当通用的模板，但是因为剪枝不够厉害，这次还有两个新的test cases 过不了
class Solution:
    def __init__(self):
        self.res = float('inf')

    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = collections.Counter(nums)
        if cnt.most_common()[0][1] > k:
            return -1

        visited = [0] * 16
        nums.sort()

        def _dfs(cur_path, idx, cur_diff):
            if len(cur_path) == n//k:
                j = 0
                while j < n and visited[j] == 1:
                    j += 1

                if j == n:
                    self.res = min(self.res, cur_diff+\
                                   (max(cur_path)-min(cur_path)))
                else:
                    visited[j] = 1
                    _dfs([nums[j]], j, cur_diff + \
                        (max(cur_path)- min(cur_path)))
                    visited[j] = 0
            else:
                # 重要的剪枝
                last = -1
                for i in range(idx, n):
                    if visited[i] == 1:
                        continue

                    if nums[i] == nums[idx]:
                        continue

                    if last != -1 and nums[i] == last:
                        continue

                    visited[i] = 1
                    _dfs(cur_path+[nums[i]], i, cur_diff)
                    last = nums[i]
                    visited[i] = 0

        visited[0] = 1
        _dfs([nums[0]], 0, 0,)

        return self.res

    """