class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root==None:

            return
        
        while root!=None:
            
            if root.val==val:

                return root
            
            if root.val>val:

                root=root.left

            else:

                root=root.right

        return None
        
