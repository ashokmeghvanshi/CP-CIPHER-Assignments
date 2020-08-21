class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val

        self.left = left

        self.right = right

class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        
        def order(root):

            if root==None:

                return 0

            else:
                l1=order(root.left)
                
                l2=order(root.right)

                return max(l1,l2)+1
                        
        length_tree = order(root)

        return length_tree
