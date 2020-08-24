class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right

class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:

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

        final_result=[]

        for i in result:

            final_result.append(i[-1])

        return final_result
