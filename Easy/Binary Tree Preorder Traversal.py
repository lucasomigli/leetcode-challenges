# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        nodes = []
        res = []
        nodes.append(root)

        while len(nodes) > 0:
            curr = nodes.pop()
            res.append(curr.val)

            if curr.right != None:
                nodes.append(curr.right)

            if curr.left != None:
                nodes.append(curr.left)

        return res
