class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26
        self.is_end_word = False
        self.char = char

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        
        for level in range(len(word)):
            idx = ord(word[level]) - ord('a')
            
            if cur_node.children[idx] is None:
                cur_node.children[idx] = TrieNode(word[level])
            
            cur_node = cur_node.children[idx]
            
        cur_node.is_end_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        
        for level in range(len(word)):
            idx = ord(word[level]) - ord('a')
            
            if cur_node.children[idx] is None:
                return False
            
            cur_node = cur_node.children[idx]
            
        if cur_node is not None and cur_node.is_end_word:
            return True
            
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        
        for level in range(len(prefix)):
            idx = ord(prefix[level]) - ord('a')
            
            if cur_node.children[idx] is None:
                return False
            
            cur_node = cur_node.children[idx]
        
        return True