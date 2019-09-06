# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        
        def recursiveCheck(nodeLeft, nodeRight):
            if nodeLeft != None and nodeRight != None and nodeLeft.val != nodeRight.val:
                return False
            elif nodeLeft == None and nodeRight == None: 
                return True
            elif nodeLeft != None and nodeRight == None:
                return False
            elif nodeLeft == None and nodeRight != None:
                return False
            else:
                print(nodeLeft.val, nodeRight.val)
                if recursiveCheck(nodeLeft.left, nodeRight.right) == False:
                    return False
                if recursiveCheck(nodeLeft.right, nodeRight.left) == False:
                    return False
                else: 
                    return True
                
        return recursiveCheck(root.left, root.right)
                    