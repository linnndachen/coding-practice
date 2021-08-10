# the reason why we are using pq is because we are always 
# looking for the smallest/lowest height
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n, = len(heightMap), len(heightMap[0])
        heap, trapped = [], 0
        
        for i in range(m):
            for j in range(n):
                if i in {0, m - 1} or j in {0, n - 1}:
                    # enque the edges
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        while heap:
            # started with the lowest height
            h, i, j = heapq.heappop(heap)
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                # looped through the enclosed area
                if 0 < x < m-1 and 0 < y < n-1 and heightMap[x][y] != -1:
                    # if there's a difference, add the area
                    trapped += max(h - heightMap[x][y], 0)
                    # increase the minimum height if needed
                    heapq.heappush(heap, (max(heightMap[x][y], h), x, y))
                    heightMap[x][y] = -1
        return trapped