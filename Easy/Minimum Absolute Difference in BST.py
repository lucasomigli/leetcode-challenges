# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        self.res = 1000000
        self.last_val = 1000000

        def getMin(node):
            if node is None:
                return
            getMin(node.left)
            self.res = min(self.res, abs(node.val - self.last_val))
            self.last_val = node.val
            getMin(node.right)

        getMin(root)
        return self.res
