class Solution:
    def __init__(self):
        self.paths = []

    def init_combo_dict(self, words):
        combo_dict = defaultdict(list)
        for w in words:
            for i in range(len(w)):
                combo_dict[w[:i] + "*" + w[i+1:]].append(w)
        return combo_dict

    def search_path(self, beginWord, cur_word, reversed_path, queue):
        if cur_word == beginWord:
            self.paths.append(list(queue))
        else:
            next_words = reversed_path[cur_word]
            for w in next_words:
                queue.appendleft(w)
                self.search_path(beginWord, w, reversed_path, queue)
        queue.popleft()

    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList or not beginWord:
            return []
        
        # step 1: cache all potential paths
        word_set = set(wordList)
        if beginWord in word_set:
            word_set.remove(beginWord)
        combo_dict = self.init_combo_dict(word_set)

        self.visited = set()
        reversed_paths, n = defaultdict(list), len(beginWord)

        ladder_words = {beginWord}
        num_of_words = 1
        found = False
        while ladder_words and not found: # stop after all shortest found
            next_ladder_words = set() # []
            for ladder_word in ladder_words:
                for i in range(n):
                    matching_word = ladder_word[:i] + "*" + ladder_word[i+1:]
                    interm_words = combo_dict[matching_word]
                    if interm_words:
                        interm_words = [w for w in interm_words if w not in self.visited]
                    if interm_words:
                        for iw in interm_words:
                            if iw == endWord:
                                # return num_of_words + 1
                                # will not break the for loop even after found to 
                                # cover all the shortest
                                found = True

                            # reversed_paths from end to begin word to simplify search path later
                            # as every path from end word must be directed to begin word
                            # but not vice versus
                            reversed_paths[iw].append(ladder_word)
                            next_ladder_words.add(iw)
            # update adds every elem in the iterable
            self.visited.update(next_ladder_words)

            # find the next ladder of words
            ladder_words = next_ladder_words
            num_of_words += 1

        if found:
            queue = deque([endWord])
            self.search_path(beginWord, endWord, reversed_paths, queue)
            return self.paths
        return []