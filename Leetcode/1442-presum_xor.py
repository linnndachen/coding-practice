class Solution:   
    # XOR
    # 1. a = b: a^b = 0
    # 2. a ^ 0 = a
    # normal preSum: sum[i:k] = prev_sum[k] - prev_sum[i-1]
    # xor presum: xor[i:k] = prev_xor[k] ^ pre_xor[i-1]

    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i, n in enumerate(arr):
            pre = n
            for k in range(i+1, len(arr)):
                pre ^= arr[k]
                if pre == 0:
                    res += k-i
        return res

    """
    def countTriplets(self, arr: List[int]) -> int:
        # O ^ 2 for understanding
        n = len(arr)
        xor_pre = [0] * (n+1)
        res = 0
        for i in range(n):
            xor_pre[i+1] = xor_pre[i] ^ arr[i]

        for i in range(1,n):
            for k in range(i+1,n+1):
                if xor_pre[i-1] == xor_pre[k]:
                    res += (k-i)
        return res

    """
    """
    def countTriplets(self, arr: List[int]) -> int:
        # O ^3 for understanding
        n = len(arr)
        xor_pre = [0] * (n+1)
        res = 0
        for i in range(n):
            xor_pre[i+1] = xor_pre[i] ^ arr[i]
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j, n):
                    a = xor_pre[i] ^ xor_pre[j] # i - j-1
                    b = xor_pre[j] ^ xor_pre[k+1] # j - k
                    
                    if a == b:
                        res += 1
        return res
    """