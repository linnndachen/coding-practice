class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select - o(N) average cases
        if not nums: 
            return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]

    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # pq - n logn
        pq = nums[:k]
        heapq.heapify(pq)
        for x in nums[k:]:
            heapq.heappush(pq, x)
            # pop out the smaller one - left side
            heapq.heappop(pq)
        return pq[0]
    """

    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nk
        n = len(nums)
        for i in range(n, n-k, -1):
            largest_idx = 0
            for j in range(i):
                if nums[j] > nums[largest_idx]:
                    largest_idx = j
            
            nums[largest_idx], nums[i-1] = nums[i-1], nums[largest_idx]
        
        return nums[n-k]
    """