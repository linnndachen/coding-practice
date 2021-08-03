class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # among all the max_sum-s in m groups, get the smallest max_sum
        # The answer must be in range
        # low = max(nums), high = sum(nums) + 1 : put everything in a group
        
        # search for the candidate C, sum(sublist) <= C
        # if the num of sublists > m, C is too small, increase lower bound
        # if the num of sublists < m, C is too big, high = C

        mini, maxi = 0 , 0
        for num in nums:
            maxi += num
            if num > mini:
                mini = num

        res = float('inf')
        while mini <= maxi:
            mid = (mini + maxi) // 2
            print(mid, mini, maxi)
            if self.is_valid(mid, nums, m):
                res = mid
                maxi = mid-1
            else:
                mini = mid+1
        return res

    def is_valid(self, x, nums, m):
        # x is mid
        numSubarrays = 1
        subarraySum = 0
        for num in nums:
            # Greedily try to add this element to the current subarray 
            # as long as the subarray's sum doesn't exceed our upper limit x
            if (num + subarraySum) <= x:
                subarraySum += num

            else:
                numSubarrays += 1
                subarraySum = num

        return (numSubarrays <= m)