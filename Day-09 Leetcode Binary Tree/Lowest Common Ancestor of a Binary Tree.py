# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def LCABT(node,p,q):

            if node==None:
                return node
            
            if node.val == p.val or node.val == q.val:
                return node
            leftnode = LCABT(node.left,p,q)
            rightnode = LCABT(node.right,p,q)
            if leftnode!=None and rightnode!=None:
                return node
            else:
                if leftnode!=None:
                    return leftnode
                else:
                    return rightnode
        
        return LCABT(root,p,q)
