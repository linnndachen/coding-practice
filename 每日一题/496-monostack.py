class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        table = {}
        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                # table[prev_item] = next bigger
                table[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            res.append(table.get(num, -1))
        return res