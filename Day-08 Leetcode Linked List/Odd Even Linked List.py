# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        
        odd_pos, even_pos, evenhead = head, head.next, head.next
        
        while odd_pos.next!=None and even_pos.next!=None:
            odd_pos.next = odd_pos.next.next
            odd_pos = odd_pos.next
            even_pos.next = even_pos.next.next
            even_pos = even_pos.next
        odd_pos.next = evenhead
        
        return head
