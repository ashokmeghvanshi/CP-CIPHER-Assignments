class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root==None:

            return root

        def breadth_first_search(root, result, level):

            if root==None:

                return root

            if len(result) == level:

                result.append([])

            result[level].append(root.val)

            breadth_first_search(root.left,  result, level + 1)

            breadth_first_search(root.right, result, level + 1)
            
            return result

        result = []
        
        result=breadth_first_search(root, result, 0)

        for i in range(len(result)):

            if i%2!=0:

                result[i]=result[i][::-1]

        return result
        
