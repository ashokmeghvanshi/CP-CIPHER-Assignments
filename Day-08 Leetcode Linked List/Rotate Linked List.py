class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None
        l=[]
        curr=head
        while curr!=None:
            l.append(curr.val)
            curr=curr.next
        
        k=k%len(l)
        l=l[-k:]+l[:-k]
        
        NewHead=None
        for element in l:
            if NewHead==None:
                NewHead = ListNode(element)
                current = NewHead
            else:
                current.next = ListNode(element)
                current = current.next
        return NewHead
    
