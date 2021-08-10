class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        filtered_dictionary = []
        for wrd in dictionary:
            if len(wrd) != len(target):
                continue
            filtered_dictionary.append(wrd)
        dictionary = filtered_dictionary
        if len(dictionary) == 0:
            return str(len(target))

        abbr = []
        self.dfs(target, 0, [], 0, abbr)
        abbr.sort(key=len)
        for w in abbr:
            if all(not self.check_ambiguity(w, word) for word in dictionary): 
                return "".join(w)
        return target


    def dfs(self, target, idx, path, count, res):
        if idx == len(target):
            path += [str(count)] if count > 0 else ""
            res.append(path)
            return

        # For each letter, we can keep accumulating count, or reset count and append letter
        self.dfs(target, idx+1, path+([str(count)] if count else [])+[target[idx]], 0, res)
        self.dfs(target, idx+1, path, count+1, res)


    def check_ambiguity(self, abbr, target):
        # Decide if abbr can be an abbreviation of s
        # Compare letter by letter
        # For each number in abbr, we can fast forward s
        i = j = 0
        while True:
            # both reached the end
            if i == len(abbr) and j == len(target): 
                return True
            # one reached the end before the other
            if i >= len(abbr) or j >= len(target): 
                return False

            if abbr[i].isdigit():
                step = int(abbr[i])
                i += 1
                j += step
            else:
                if abbr[i] != target[j]: 
                    return False
                i += 1
                j += 1
        return True