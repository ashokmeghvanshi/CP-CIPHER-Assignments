# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        
        frist_ptr=head
        second_ptr=head.next
        while frist_ptr!=None and second_ptr!=None:
            frist_ptr.val,second_ptr.val=second_ptr.val,frist_ptr.val
            frist_ptr=second_ptr.next
            
            if frist_ptr==None:
                break
            second_ptr=second_ptr.next.next
    
        return head
