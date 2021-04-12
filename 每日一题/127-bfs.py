class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        graph, n = collections.defaultdict(list), len(beginWord)

        for idx, val in enumerate(wordList):
            for i in range(n):
                key = val[:i] + "*" + val[i+1:]
                graph[key].append(val)
        
        queue, seen = deque([(beginWord, 1)]), set()

        while queue:
            cur_w, steps = queue.popleft()

            for i in range(n):
                option = cur_w[:i] + "*" + cur_w[i+1:]
                
                for connected_w in graph[option]:
                    if connected_w == endWord:
                        return steps + 1
                    
                    if connected_w not in seen:
                        queue.append((connected_w, steps+1))
                        seen.add(connected_w)
                    
                graph[option] = []

        return 0
