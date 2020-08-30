# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def createbst(preorder,inorder, sindex, eindex): 

            if sindex>eindex:
                return None

            newnode = TreeNode(preorder[self.count]) 
            self.count= self.count+1

            if sindex == eindex : 
                return newnode 

            newindex =inorder.index(newnode.val) 
            newnode.left = createbst(preorder,inorder, sindex, newindex-1) 
            newnode.right = createbst(preorder,inorder,newindex + 1, eindex)
            return newnode
        
        self.count=0
        
        newnode1=createbst(preorder,inorder,0,len(preorder)-1)
        return newnode1
