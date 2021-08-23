class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        product = 0
        for n in nums:
            product ^= n

        # the right most bit - the difference between a & b
        diff = product & (-product)

        x = 0
        for n in nums:
            # 如果 n 的最后一位正好是diff
            # 其他 even 次数的即使match，也会被抵消
            if n & diff:
                x ^= n

        return [x, product^x]