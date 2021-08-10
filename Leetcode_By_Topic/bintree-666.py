class Solution(object):
    def pathSum(self, nums):
        self.res = 0
        # {dep,pos: val}
        values = {x // 10: x % 10 for x in nums}
        self.dfs(nums[0]//10, 0, values)
        return self.res

    def dfs(self, node, cur_sum, values):
        if node not in values:
            return

        cur_sum += values[node]
        depth, pos = divmod(node, 10) # 1, 1

        left = (depth+1)*10 + 2*pos - 1 # 21 - dep,pos
        right = left + 1 # 22 - dep,pos

        # leaf node: the leaf nodes contain sum of the entire path from root to each leaf nodes
        if left not in values and right not in values:
            self.res += cur_sum

        else:
            self.dfs(left, cur_sum, values)
            self.dfs(right, cur_sum, values)

    """
    # bottom-up: for understanding
    def pathSum(self, nums):
        # nodes: count
        s = {}
        # root: path sum
        l = {}

        # starting with leaf node
        for i in nums[::-1]:
            dep, pos, val = i // 100, i // 10 % 10, i % 10
            # root's count: max(1, left's count + right's count)
            l[dep, pos] = max(1, l.get((dep + 1, pos * 2 - 1), 0) + l.get((dep + 1, pos * 2), 0))
            # root's path sum = (root count * root val) + left's path sum + right's path sum
            s[dep, pos] = s.get((dep + 1, pos * 2 - 1), 0) + s.get((dep + 1, pos * 2), 0) + l[dep, pos] * val
        return s.get((1, 1), 0)
    """