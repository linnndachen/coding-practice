# a - steps to the right, b - steps to the left
# x - target, we are at 0. return the minimum number of jumps
class Solution:
    """
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # furtherest it can go
        max_val = max([x] + forbidden) + a + b
        jumps = [0] + [math.inf] * max_val

        for pos in forbidden:
            jumps[pos] = -1
        # keeping track of the positions we are visiting
        queue = deque([0])

        while queue:
            pos = queue.popleft()
            # jumps[pos+a] will always be infinity if we have never visited
            if pos + a <= max_val and jumps[pos+a] > jumps[pos] + 1:
                queue.append(pos + a)
                # jumps[pos] + 1 is the jumps we have made so far
                jumps[pos+a] = jumps[pos] + 1
            
            if pos - b > 0 and jumps[pos-b] > jumps[pos] + 1:
                jumps[pos-b] = jumps[pos] + 1
                
                # take a step back and move forward
                if pos-b+a <= max_val and jumps[pos-b+a] > jumps[pos] + 2:
                    queue.append(pos - b + a)
                    jumps[pos-b+a] = jumps[pos] + 2

        return jumps[x] if jumps[x] < math.inf else -1
        """
        

    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        bound = max([x] + forbidden) + a + b
        # positions, jumps, directions
        queue = [(0, 0, False)]
        
        F = {(pos, direct) for pos in forbidden for direct in (True, False)}

        for pos, jump, direct in queue:
            if pos == x: 
                return jump

            # if out of bound or in forbidden
            if pos > bound or (pos, direct) in F: 
                continue
            
            # add seen to forbidden
            F.add((pos, direct))
            queue.append((pos + a, jump + 1, True))
            
            if direct and pos - b > 0:
                queue.append((pos - b, jump + 1, False))


        return -1