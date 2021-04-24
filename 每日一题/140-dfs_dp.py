class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordset = set(wordDict)
        self.memo = collections.defaultdict(list)
        self.backtrack(s, wordset)

        return [" ".join(words) for words in self.memo[s]]

    def backtrack(self, s, wordset):
        if not s:
            return [[]]

        if s in self.memo:
            return self.memo[s]

        for right in range(1, len(s)+1):
            word = s[:right]
            if word in wordset:
                for sub in self.backtrack(s[right:], wordset):
                    self.memo[s].append([word] + sub)

        return self.memo[s]