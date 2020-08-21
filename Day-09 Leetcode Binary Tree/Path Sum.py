class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:
    
    def hasPathSum(self, root: TreeNode, sum1: int) -> bool:
        
        if root==None:

            return False
        
        def path(root,sum1):
            
            if root==None:

                return False
            
            if root.val==sum1 and root.left==None and root.right==None:

                return True
        
            return path(root.right,sum1-root.val) or path(root.left,sum1-root.val)
                
        return path(root,sum1)
