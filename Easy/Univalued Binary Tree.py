class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = []

        def dfs(node):
            if node:
                stack.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(stack)) == 1
