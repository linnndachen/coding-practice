from typing import List

class Solution:
    """
    这道题的递归可以分为两个方式，一个是按照人来递归，一个是按照tasks。一开始我的approach
    是按照人，但是按照人需要用state记忆，而且不好剪枝。这个题对递归的处理有比较深刻的体会。
    """
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        if len(jobs) <= k:
            return jobs[0]

        left, right = jobs[0], sum(jobs)
        while left < right:
            mid = (left+right) // 2

            buckets = [0] * k
            if self._possible(mid, buckets, 0, jobs):
                right = mid
            else:
                left = mid + 1

        return left


    def _possible(self, target, buckets, i, jobs):
            if i == len(jobs):
                return True

            for j in range(len(buckets)):

                if buckets[j] + jobs[i] > target:
                    continue

                buckets[j] += jobs[i]
                if self._possible(target, buckets, i+1, jobs): 
                    return True

                buckets[j] -= jobs[i]

                # 重要剪枝 - 
                # 如果有12个空闲的工人，分配给任何一个人剩下的路都是一样的
                # 反之，如果这个task不可以分配给其中一个，剩下的尝试也是没用的
                if buckets[j] == 0: 
                    break

            return False

    """
    # my original dfs. I think this is wrong because after I sorted the
    # jobs and do this greedly, it will run into problem.
    # Because it tries to add all the big ones first. However, it 
    # should be each k get a big one. Thus, I need to have an arr
    # to remeber everyone' current workload and iterate it. 
    # 如果我用这种一个人一个人来处理的办法，可以用状态压缩，残酷群群主里说的第二种办法
    # 每一个人要iterate 所有没有被taken care的tasks
    
    def _dfs(self, target, i, cur, jobs, k):
        if i == len(jobs):
            return True

        if cur + jobs[i] <= target:
            if self._dfs(target, i+1, cur+jobs[i], jobs, k):
                return True
        else:
            if k > 0:
                if self._dfs(target, i+1, jobs[i], jobs, k-1):
                    return True

        return False
    """