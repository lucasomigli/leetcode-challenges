# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def iterate(node, count):
            if not node:
                return
            if node.left == None and node.right == None and node.val == count:
                return True

            return iterate(node.left, count - node.val) or iterate(node.right, count - node.val)
        return iterate(root, sum)
