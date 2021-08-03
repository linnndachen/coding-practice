class WordFilter:

    def __init__(self, words: List[str]):
        self.inputs = {}
        for idx, word in enumerate(words):
            prefix = ""
            
            for char in [""] + list(word):
                prefix += char
                suffix = ""
                
                for char in [""] + list(word[::-1]):
                    suffix += char
                    self.inputs[prefix + '#' + suffix[::-1]] = idx
                    
    def f(self, prefix: str, suffix: str) -> int:
        return self.inputs.get(prefix + '#' + suffix, -1)
