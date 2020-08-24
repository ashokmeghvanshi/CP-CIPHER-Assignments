def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        def preorder(root,l):

            if root==None:

                return 
            
            l.append(root.val)
            
            preorder(root.left,l)

            preorder(root.right,l)

        l=[]

        preorder(root,l)

        return l
