class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:
    
    def findTilt(self, root: TreeNode) -> int:

        if root==None:

            return 0
         
        self.result = 0
        
        def pathsum(node):

            if not node:

                return 0

            left = pathsum(node.left)

            right = pathsum(node.right)
            
            self.result = self.result+abs(left - right)
            
            return node.val + left + right
        
        pathsum(root)
        
        return self.result
