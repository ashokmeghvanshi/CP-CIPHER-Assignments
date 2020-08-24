class TreeNode:

   def __init__(self, val=0, left=None, right=None):

         self.val = val         self.left = left

        self.right = right

class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:

        def postorder(root,l):

            if root==None:

                return 
            
            postorder(root.left,l)

            postorder(root.right,l)
            
            l.append(root.val)
            

        l=[]

        postorder(root,l)

        return l
