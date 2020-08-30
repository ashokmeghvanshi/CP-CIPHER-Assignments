# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root==None:
            return 0
        
        self.path = float("-inf")
        def maxpath(newnode):
            if newnode==None:
                return 0
            leftnode=maxpath(newnode.left)
            rightnode=maxpath(newnode.right)
            leftpath =max(leftnode,0)
            rightpath =max(rightnode,0)
            
            self.path = max(self.path,newnode.val+leftpath + rightpath)
            
            return max((newnode.val + leftpath), (newnode.val + rightpath))
        
        maxpath(root)
        return self.path
