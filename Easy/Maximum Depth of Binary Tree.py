# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            right = self.maxDepth(root.right)
            left = self.maxDepth(root.left)

            return 1 + max(right, left)
