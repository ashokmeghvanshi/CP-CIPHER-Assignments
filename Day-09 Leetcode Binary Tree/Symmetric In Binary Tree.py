class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        
        def Symmetric_check(root1,root2):

            if root1==None and root2==None:

                return True
            
            if ((root1!=None and root2!=None) and (root1.val==root2.val)):

                return Symmetric_check(root1.left,root2.right) and Symmetric_check(root1.right,root2.left)
            
            return False
        
        return Symmetric_check(root,root)
