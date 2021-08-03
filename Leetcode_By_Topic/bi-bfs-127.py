import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        n = len(beginWord)
        wordBank = collections.defaultdict(list)

        for word in wordList:
            for i in range(n):
                wordBank[word[:i]+"*"+word[i+1:]].append(word)

        beginQueue = collections.deque([beginWord])
        endQueue = collections.deque([endWord])
        visited = set(beginWord)
        step = 0
        while beginQueue and endQueue:
            step += 1
            if len(beginQueue) > len(endQueue):
                beginQueue, endQueue = endQueue, beginQueue

            for _ in range(len(beginQueue)):
                cur = beginQueue.popleft()
                for i in range(n):
                    tmpt = cur[:i] +'*' + cur[i+1:]

                    for word in wordBank[tmpt]:
                        if word in endQueue:
                            return step + 1
                        
                        if word not in visited:
                            beginQueue.append(word)
                            visited.add(word)
        else:
            return 0

    """
    # clearer but longer version
    
    def __init__(self):
        self.length = 0
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # if the met
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None


    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)
        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queues for birdirectional BFS
        queue_begin = deque([(beginWord, 1)]) # BFS starting from beginWord
        queue_end = deque([(endWord, 1)]) # BFS starting from endWord

        # {unique_word: steps/level}
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None
        
        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0
    """