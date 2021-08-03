class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # using a heapq structure, while all the dist are smallest 
        # queue[0] is the same, it will automatically ranked by the second element
        # which is in lexi order
        m, n = len(maze), len(maze[0])
        seen = {(ball[0], ball[1]): [0, ""]}

        queue = [(0, "", ball[0], ball[1])]

        while queue:
            d, path, i, j = heapq.heappop(queue)
            if [i, j] == hole:
                return path

            for dx, dy, di in [(-1, 0, 'u'), (0, 1, 'r'), 
                               (0, -1, 'l'), (1, 0, 'd')]:
                x, y, dist = i, j, 0
                while 0 <= x+dx < m and 0 <= y+dy < n and maze[x+dx][y+dy] != 1:
                    x, y, dist = x+dx, y+dy, dist+1
                    
                    if [x, y] == hole:
                        break
                    
                if (x, y) not in seen or [d+dist, path+di] < seen[(x, y)]:
                    seen[(x, y)] = [d+dist, path+di]
                    heapq.heappush(queue, (d+dist, path+di, x, y))

        return "impossible"