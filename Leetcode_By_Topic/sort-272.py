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
                # move smaller difference values to the left
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
                # increase the range
                quickselect(true_idx, right)
            else:
                # squeeze the range
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

    """
    # bucket sort - wrong answer
    # we cannot use bucket sort here because we are detailed to float nums
    # while buckets are divided by whole number
    # Therefore, when we have numers like 2, 3 compare with 2.571429. 
    # We will have the wrong answer
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        nums = inorder(root)
        dist = lambda idx: abs(nums[idx] - target)

        counter = collections.defaultdict(list)
        maxdist = 0
        for idx, val in enumerate(nums):
            diff = dist(idx)
            counter[diff].append(val)
            maxdist = max(maxdist, diff)

        bucket = [[] for _ in range(int(maxdist) + 1)]
        for dist, n in counter.items():
            bucket[int(dist)].extend(n)

        flat_list = [item for sublist in bucket for item in sublist]

        return flat_list[:k]
    """