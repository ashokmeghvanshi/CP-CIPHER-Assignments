class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        self.siblings(root, x, y)
        
        if(self.height(root, x, 0) == self.height(root, y, 0) and (not(self.siblings(root, x, y)))):

            return True

        else:

            return False
        
    def siblings(self, root: TreeNode, a:int, b:int):

        if root==None:

            return 0
        
        if(root.left!=None and root.right!=None):
            
            left = root.left.val
            
            right = root.right.val
            
            if((left == a and right == b) or (left == b and right == a)):

                return True
            
        return (self.siblings(root.left, a, b) or self.siblings(root.right, a, b))

    def height(self,root: TreeNode, x: TreeNode, h):
        
        if root==None:

            return 0
        
        if root.val == x:

            return h
        
        length = self.height(root.left, x, h+1)
        
        if length!=0:

            return length
        
        return self.height(root.right, x, h+1)
