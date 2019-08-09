class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        def equal(node_left, node_right):
            if node_left is None and node_right is None:
                return True
            elif node_left is None or node_right is None:
                return False
            elif node_left.val != node_right.val:
                return False
            return equal(node_left.left, node_right.right) and equal(node_right.left, node_left.right)

        if not root:
            return True
        return equal(root.left, root.right)
