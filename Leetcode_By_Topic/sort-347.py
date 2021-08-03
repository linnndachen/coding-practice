from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for x in nums:
            counts[x] = counts.setdefault(x, 0) + 1

        items = list(counts.items())
        return [c[0] for c in self.partition(items, 0, len(items)-1, k)]

    def partition(self, items, left, right, k):
        if left == right:
            return items

        pivot_idx = random.randint(left, right)
        items[right], items[pivot_idx] = items[pivot_idx], items[right]

        # partition
        mid = items[right][1]

        i = left
        # j is the store idx
        j = left

        while i < len(items):
            # move all bigger item to the right
            if items[i][1] > mid:
                items[i], items[j] = items[j], items[i]
                j += 1
            i += 1
        # move the pivot, where we put at the end back to the correct point
        items[j], items[right] = items[right], items[j]

        if j+1 == k:
            return items[:k]
        if j+1 < k: # go right
            return self.partition(items, j+1, right, k)
        if j+1 > k: # go left
            return self.partition(items, left, j, k)

    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        counter, maxfreq = collections.defaultdict(int), 0

        for n in nums:
            counter[n] += 1
            maxfreq = max(maxfreq, counter[n])

        bucket = [[] for _ in range(maxfreq + 1)]

        for num, freq in counter.items():
            bucket[freq].append(num)

        flat_list = [item for sublist in bucket for item in sublist]

        return flat_list[::-1][:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap
        if k == len(nums):
            return nums
        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)
        # max_heap = [(-val, key) for key, val in dic.items()]
        # heapq.heapify(max_heap)
        # for i in range(k):
            # res.append(heapq.heappop(max_heap)[1])
        # return res
    """