class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # factorials
        factorials, nums = [1], ["1"]

        for i in range(1, n):# 1,2,3
            factorials.append(factorials[i-1]*i)
            # 1*1, 1*2, 2*3 = [1,2,6]
            nums.append(str(i+1))

        k -= 1
        res = []

        for i in range(n-1, -1, -1):
            cur = k // factorials[i]
            k -= cur * factorials[i]

            res.append(nums[cur])
            del nums[cur]

        return "".join(res)

    # 4, 9
    # 1234 
    # 1243
    # 1324 
    # 1342
    # 1432 
    # 1423 -> 3 * 2 * 1