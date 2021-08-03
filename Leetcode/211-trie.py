class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = collections.defaultdict(set)
        

    def addWord(self, word: str) -> None:
        self.trie[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        
        word_len = len(word)
        
        for w in self.trie[word_len]:
            i = 0
            while i < word_len and (w[i] == word[i] or word[i] == '.'):
                i += 1
            
            if i == word_len:
                return True
        
        return False
            