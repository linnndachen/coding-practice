class SegTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):
        self.root = self._buildtree(0, len(nums)-1, nums)


    def _buildtree(self, start, end, vals):
        # Time - O(n)
        if start == end: # reached a leaf node
            node = SegTreeNode(start, end)
            node.total = vals[start]
            return node

        mid = (start + end) // 2
        root = SegTreeNode(start, end)

        root.left = self._buildtree(start, mid, vals)
        root.right = self._buildtree(mid+1, end, vals)

        root.total = root.left.total + root.right.total

        return root


    def update(self, index: int, val: int) -> None:
        # the update val is a leaf node
        return self._updateHelper(self.root, index, val)

    def _updateHelper(self, root, idx, val):
        # Time - O(n)
        if root.start == root.end == idx:
            root.total = val
            return val

        mid = (root.start + root.end) // 2

        if idx > mid:
            # right subtree
            self._updateHelper(root.right, idx, val)
        else:
            self._updateHelper(root.left, idx, val)


        root.total = root.left.total + root.right.total
        return root.total


    def sumRange(self, left: int, right: int) -> int:
        # Time - O(logn + k)
        return self._sumRangeHelper(self.root, left, right)

    def _sumRangeHelper(self, root, low, hi):
        # case 1:
        if root.start == low and root.end == hi:
            return root.total

        mid = (root.start + root.end) // 2

        if hi <= mid:
            # whole range on the left
            return self._sumRangeHelper(root.left, low, hi)

        # whole range on the right
        elif low >= mid + 1:
            return self._sumRangeHelper(root.right, low, hi)

        # cross left and right and need to split
        else:
            return self._sumRangeHelper(root.left, low, mid) + \
                    self._sumRangeHelper(root.right, mid+1, hi)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)