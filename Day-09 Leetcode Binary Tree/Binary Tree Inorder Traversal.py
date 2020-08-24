class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def inorder(root,l):

            if root==None:

                return 

            inorder(root.left,l)

            l.append(root.val)

            inorder(root.right,l)

        l=[]

        inorder(root,l)

        return l
        
