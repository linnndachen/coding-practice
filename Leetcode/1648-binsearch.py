class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # counting the balls sold
        def _count(nums, k):
            res = 0
            for i in range(len(nums)):
                if nums[i] < k:
                    break

                res += nums[i] - k + 1

            return res

        # 1. sort
        inventory.sort(reverse=True)
        left, right = 1, inventory[0]

        # 2. find the lowest k it can get to
        while left < right:
            mid = (left + right) // 2
            
            if _count(inventory, mid) <= orders:
                right = mid
            else:
                left = mid + 1

        M = 1000000007
        res = 0

        # 3. add all the full counts
        k = left
        for idx, val in enumerate(inventory):
            if val < k:
                break
            res += (val + k) * (val - k + 1) // 2

        # 4. add the left overs
        rest = orders - _count(inventory, k)
        res += (k-1) * rest

        return res % M

    """
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # 5, 4, 3, 2
        inventory.sort(reverse=True) # inventory high to low 
        inventory += [0]
        ans = 0
        k = 1
        for i in range(len(inventory)-1): 
            if inventory[i] > inventory[i+1]: 
                if k*(inventory[i] - inventory[i+1]) < orders: 
                    ans += k*(inventory[i] + inventory[i+1] + 1)\
                            *(inventory[i] - inventory[i+1])//2 # arithmic sum 
                    orders -= k*(inventory[i] - inventory[i+1])
                else: 
                    q, r = divmod(orders, k)
                    ans += k*(2*inventory[i] - q + 1) * q//2 + r*(inventory[i] - q)
                    return ans % 1_000_000_007
            k += 1
    """