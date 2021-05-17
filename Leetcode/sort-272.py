# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        def partition(left, right, pivot_idx):
            pivot = dist(pivot_idx)
            # move to the end
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            store_idx = left

            for i in range(left, right):
                # move smaller values to the left
                if dist(i) < pivot:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1

            # put the pivot back to the right idx
            nums[right], nums[store_idx] = nums[store_idx], nums[right]
            return store_idx

        def quickselect(left, right):
            if left == right:
                return

            pivot_idx = random.randint(left, right)
            true_idx = partition(left, right, pivot_idx)

            if true_idx == k:
                return

            if true_idx < k:
                # go left
                quickselect(true_idx, right)
            else:
                # go right
                quickselect(left, true_idx)
    
        nums = inorder(root)
        dist = lambda idx: abs(nums[idx] - target)
        quickselect(0, len(nums)-1)
        return nums[:k]

    """
    # heap solution - Nlogk
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        heap = []

        def inorder(node):
            if not node:
                return 

            inorder(node.left)
            heappush(heap, (-abs(node.val-target), node.val))

            if len(heap) > k:
                heappop(heap)

            inorder(node.right)

        inorder(root)
        return [x for _, x in heap]
    """