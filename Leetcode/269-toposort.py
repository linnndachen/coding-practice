from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # the first letter would be - no other letters smaller than it
        # then after removing the first letter, 
        # find the second one w/ no smaller letters
        graph, degree = self.build_graph(words)

        source = deque()
        for key in degree:
            if degree[key] == 0:
                source.append(key)

        res = []
        while source:
            char = source.popleft()
            res.append(char)

            for child in graph[char]:
                degree[child] -= 1
                if degree[child] == 0:
                    source.append(child)

        if len(res) < len(degree):
            return ""

        return ''.join(res)

    def build_graph(self, words):
        graph, degree = {}, {}
        
        # add vertices
        for w in words:
            for char in w:
                if char in graph:
                    continue
                graph[char] = []
                
                if char in degree:
                    continue
                degree[char] = 0

        # build graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # a flag to prevent cases like "abc", "ab"
            # while "ab", "abc" is okay
            found = False
            for i in range(min_len):
                if w1[i] != w2[i]:
                    # w1[i] < w2[i]
                    if w2[i] not in graph[w1[i]]:
                        graph[w1[i]].append(w2[i])
                        degree[w2[i]] += 1
                    found = True
                    break

            if found == False and len(w1) > len(w2):
                return "", ""
        return graph, degree