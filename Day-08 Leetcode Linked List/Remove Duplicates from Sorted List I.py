# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        head1=head
        head2=head1
        while head1!=None and head1.next!=None:
            if head1.val==head1.next.val:
                head1.next=head1.next.next
            else:
                head1=head1.next
            
        return head2
                
