# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        def reverse(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            if node.right != None:
                reverse(node.right)
            if node.left != None:
                reverse(node.left)
        reverse(root)
        return root
