class Solution:
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        
        for num in nums:
            if num - 1 not in nums:
                cur_n = num
                cur_len = 1
                
                while cur_n + 1 in nums:
                    cur_n += 1
                    cur_len += 1
                
                res = max(res, cur_len)
        
        return res
    """


    def longestConsecutive(self, nums: List[int]) -> int:
        def find(p):
            while p != parents[p]:
                parents[p] = find(parents[p])
                p = parents[p]
            return p

        def union(p, q):
            i, j = find(p), find(q)

            if i != j:
                if rank[i] > rank[j]:
                    parents[j] = i
                elif rank[j] < rank[i]:
                    parents[i] = j
                else:
                    parents[i] = j
                    rank[j] += 1

        if not nums:
            return 0

        parents, rank = {}, {}
        nums = set(nums)

        for num in nums:
            parents[num] = num
            rank[num] = 0

        for num in nums:
            if num-1 in nums:
                union(num-1, num)
            if num+1 in nums:
                union(num+1, num)

        d = collections.defaultdict(int)
        for num in nums:
            d[find(num)] += 1

        return max([n for n in d.values()])