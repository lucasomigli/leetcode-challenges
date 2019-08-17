# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def isSame(left, right):
            if left is None or right is None:
                return left == right

            if left.val != right.val:
                return False

            if isSame(left.left, right.left) == False:
                return False
            if isSame(left.right, right.right) == False:
                return False

            return True

        return isSame(p, q)
