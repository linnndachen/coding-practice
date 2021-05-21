class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left < right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = (left+right) // 2 # [1,2]

            if nums[mid] == target:
                return True

            # [4,5,6, 7,    0, 1,2]
            #  L   M  T(L')  M   R
            if nums[mid] > nums[right]: # on the left side:
                if target < nums[mid] and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        if left == right and nums[left] == target:
            return True

        return False