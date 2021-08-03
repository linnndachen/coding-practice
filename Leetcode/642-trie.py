from collections import defaultdict
class TrieNode():
    def __init__(self):
        self.children = defaultdict(list)
        self.isEnd = False
        self.hot = 0

class AutocompleteSystem:
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

    def __init__(self, sentences: list[str], times: list[int]):
        self.root = TrieNode()
        self.searchTerm = ""
        
        # add existing data
        for i, sentence in enumerate(sentences):
            self.add(sentence, times[i])

    def add(self, sentence, hot):
        node = self.root
        
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.isEnd = True
        # store in negation so that can sort in ascending order later
        node.hot -= hot

    def search(self):
        node = self.root
        res = []
        path = ""

        for c in self.searchTerm:
            if c not in node.children:
                return res

            # add each character to path variable, path will added to res 
            # when we found node.isEnd ==True
            path += c
            node = node.children[c]

        # search for the rest
        # if search term is "i_a", we are at "a" node.
        self.dfs(node, path, res)

        return [item[1] for item in sorted(res)[:3]]

    def dfs(self, node, path, res):
        # base case
        if node.isEnd:
            res.append((node.hot, path))

        for c in node.children:
            self.dfs(node.children[c], path+c, res)

    def input(self, c: str) -> List[str]:
        if c != "#":
            self.searchTerm += c
            return self.search()

        else: # reset
            self.add(self.searchTerm, 1)
            self.searchTerm = ""