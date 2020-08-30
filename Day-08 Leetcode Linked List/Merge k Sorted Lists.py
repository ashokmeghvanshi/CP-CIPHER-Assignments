# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists==None:
            return []
        root = ListNode(0)
        list_arr = []
        for i in lists:
            head=i
            while head!=None:
                list_arr.append(head.val)
                head =  head.next        
        list_arr=sorted(list_arr)
        new_node = root
        for i in range(len(list_arr)): 
            new_node.next = ListNode(list_arr[i])
            new_node = new_node.next
        return root.next
