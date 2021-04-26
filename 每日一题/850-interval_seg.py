# The difference between this one and the skyline problem is that skyline problem's height 
# always start with 0. However, for this one, the rectangles might be at any given height.
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # 1: Populate events
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()
        
        # 2: helper function to get the width of a tempt area - technique same as merge interval
        def get_width():
            width = 0
            prev_x = -1
            for x1, x2 in active:
                prev_x = max(prev_x, x1)
                width += max(0, x2 - prev_x)
                prev_x = max(prev_x, x2)
            return width

        # 3: sweep the line to realize the area
        # it doesn't make a difference to use heap because we need to remove by idx
        active = []
        cur_y = events[0][0]
        ans = 0
        for y, typ, x1, x2 in events:
            # For all vertical ground covered, update answer
            ans += get_width() * (y - cur_y)

            # Update active intervals
            if typ is OPEN:
                active.append((x1, x2))
                active.sort()
            else:    
                active.remove((x1, x2))

            cur_y = y

        return ans % (10**9 + 7)

    """
    def rectangleArea(self, r):
        arr = [i for x1, y1, x2, y2 in r for i in [[x1,y1,y2,0],[x2,y1,y2,1]]]
        ans, prev_x = 0, arr[0][0]
        heap = [(float("inf"), float("inf"))] # y1, y2
        
        for cur_x, y1, y2, closed in sorted(arr):
            h = low = high =  0
            
            # imagine a line sweeping from the sky to the ground
            # scan to get the height
            for (cur_low, cur_high) in heap:
                # a completely new area
                if cur_low > high:
                    h += high - low
                    low, high = cur_low, cur_high
                else:
                    high = max(high, cur_high)

            ans += (cur_x - prev_x) * h 
            heap.remove((y1,y2)) if closed else bisect.insort(heap,(y1,y2))
            prev_x = cur_x 
        return ans % (10 ** 9 + 7)
    """