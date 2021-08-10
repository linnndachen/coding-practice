class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        self.backtrack(nums, res, [], used)
        return res

    def backtrack(self, nums, res, path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, res, path, used)

            path.pop()
            used[i] = False

    """
    def dfs(self, options, path, res):
        # base case: when there's no options/nums to choose from
        if not options:
            res.append(path)

        # Relation:
        for i in range(len(options)):
            # options are anything expect [i] itself
            # path + the current [i]
            self.dfs(options[:i] + options[i+1:], path+[options[i]], res)
    """