class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack, trails = [], len(nums) - k

        for val in nums:
            while stack and val < stack[-1] and trails > 0:
                stack.pop()
                trails -= 1

            stack.append(val)
        return stack[:k]