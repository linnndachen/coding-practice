class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, options, path, res):
        # base case: when there's no nums to choose from
        if not options:
            res.append(path)

        # Relation:
        for i in range(len(options)):
            # options are anything expect [i] itself
            # path + the current [i]
            self.dfs(options[:i] + options[i+1:], path+[options[i]], res)
