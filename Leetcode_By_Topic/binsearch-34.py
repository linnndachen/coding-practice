class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        n, res = len(nums), []

        left, right = 0, n-1

        # find left num   .....----....
        while left < right:
            mid = (left+right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                right = mid
        if left == right and nums[left] == target:
            res.append(left)
        else:
            res.append(-1)


        # find the right num     .....----....
        left, right = 0, n-1
        while left < right:
            mid = (left+right) // 2 + 1
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid

        if left == right and nums[left] == target:
            res.append(left)
        else:
            res.append(-1)

        return res