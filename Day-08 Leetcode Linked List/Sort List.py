# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l=sorted(l)
        
        l3=ListNode()
        temp=l3
        for i in range(len(l)):
            temp.val=l[i]
            if i!=len(l)-1:
                temp.next=ListNode()
                temp=temp.next
            
        return l3
