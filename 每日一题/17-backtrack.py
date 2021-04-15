class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # corner case:
        if len(digits) == 0:
            return []

        table = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'}
        res = []
        self.backtrack(digits, table, 0, [], res)
        return res

    def backtrack(self, digits, table, idx, path, res):
        if len(path) == len(digits):
            res.append("".join(path))
            return
        
        candy = table[digits[idx]]
        for letter in candy:
            path.append(letter)
            self.backtrack(digits, table, idx+1, path, res)
            path.pop()