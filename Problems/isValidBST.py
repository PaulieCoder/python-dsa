# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ValidBST:
    def isValidBST(self, root):
        
        def isValidBSTHelper(node, minLimit, maxLimit):
            if node is None:
                return True
            else:
                if(minLimit < node.val <= maxLimit):
                    if(isValidBSTHelper(node.left, minLimit, node.val) and
                        isValidBSTHelper(node.right, node.val, maxLimit)):
                        return True
                    else: 
                        return False
                else:
                    return False
        
        return isValidBSTHelper(root, float("-inf"), float("inf"))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

ValidBST().isValidBST(root)