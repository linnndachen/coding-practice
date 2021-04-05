class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        # k new stations, insert k so that the maximum distance is minimized
        # min(max(distances between 2 stations))

        def possible(dis):
            # how many new stations do we need to insert so that 
            # each distance is smaller than the "dis"
            new_station = 0
            for i in range(len(stations) - 1):
                new_station += (stations[i+1] - stations[i]) // dis         
            return new_station <= k

        low, hi = 0, stations[-1] - stations[0]
        while hi - low > 1e-6:
            mid = (low + hi) / 2.0
            if possible(mid):
                hi = mid
            else:
                low = mid

        return low