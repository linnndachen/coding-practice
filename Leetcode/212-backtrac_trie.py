"""
base case: 
    if the cur_word is in words, append to result

relationship:
    go right or down to see if the next alphabet matches

    if it matches, call the recursion to complete the word, 
        if it doesn't, continue to move

The catch:
    There's a list of words -> we build a trie
"""
class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = defaultdict(TrieNode)
        self.end_word = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #self.board = board
        # build trie tree
        self.root = TrieNode()
        self.build_tree(words)

        # dfs
        m, n = len(board), len(board[0])

        res = []
        visited = set()
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, self.root, m, n, res, "", board, visited)
        return res

    def build_tree(self, words):
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    new_node = TrieNode(char)
                    node.children[char] = new_node
                node = node.children[char]
            # put end word flag
            node.end_word = True

    def dfs(self, i, j, node, m, n, res, cur, board, visited):
        if (i, j, cur) in visited:
            return

        char = board[i][j]
        if char in node.children:
            visited.add((i, j, cur))
            # mark as visited
            board[i][j]="#"
            cur += char

            # check if end word
            if node.children[char].end_word:
                res.append(cur)
                node.children[char].end_word=False
                
            for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                x, y = i+dx, j+dy
                if 0 <= x < m and 0<= y < n:
                    self.dfs(x, y, node.children[char], m, n, res, cur, board, visited)

            board[i][j]=char