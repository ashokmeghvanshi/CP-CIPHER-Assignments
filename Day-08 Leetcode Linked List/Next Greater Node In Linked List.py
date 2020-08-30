# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head==None:
            return head
        node_list = []
        start = head
        while start!=None:
            node_list.append(start.val)
            start = start.next
        stack = []
        result = [0]*len(node_list)
        for i in range(len(node_list)):
            while stack==None and(node_list[stack[-1]] < node_list[i]):
                result[stack.pop(-1)] = node_list[i]
            stack.append(i)
        return result
            
