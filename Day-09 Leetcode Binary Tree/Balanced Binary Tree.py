class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:

    def isBalanced(self, root: TreeNode) -> bool:

        if root==None:

            return True
        
        def height(root):

            if root is None:

                return 0

            return max(height(root.left),height(root.right)) + 1
        
        def Balanced_Check(root):
            
            if root==None:

                return True

            lh=height(root.left)

            rh=height(root.right)
    
            if (abs(lh-rh)<=1) and (Balanced_Check(root.left)==True and Balanced_Check(root.right)==True):

                return True

            return False

        return Balanced_Check(root)
