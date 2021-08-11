# Time - O(N * 2^l) (l is how many char in the string)
# Space - O(N) + O(N * 2^l) (stack + soluion)
class Solution: 
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.backtrack(S, res, [], 0)
        return res

    def backtrack(self, S, res, path, idx):
        if idx == len(S):
            res.append("".join(path[:]))
            return

        if S[idx].isdigit():
            path.append(S[idx])
            self.backtrack(S, res, path, idx+1)      
        else:
            path.append(S[idx].lower())
            self.backtrack(S, res, path, idx+1)
            path.pop()
            
            path.append(S[idx].upper())
            self.backtrack(S, res, path, idx+1)

        path.pop()

    """
    # bfs
    def letterCasePermutation(self, S: str) -> List[str]:
        queue = collections.deque()

        # enque the first element
        if S[0].isdigit():
            queue.append(S[0])
        else:
            queue.append(S[0].lower())
            queue.append(S[0].upper())

        for char in S[1:]:
            for _ in range(len(queue)):
                prev = queue.popleft()
                
                if char.isdigit():
                    queue.append(prev + char)
                else:
                    queue.append(prev + char.lower())
                    queue.append(prev + char.upper())

        return list(queue)
        """