# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    result = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        self.check_sum(root, sum)
        return self.result

    def check_sum(self, root, sum):
        if root is None:
            return
        if root.val == sum:
            self.result += 1
        self.check_sum(root.left, sum - root.val)
        self.check_sum(root.right, sum - root.val)
        return
