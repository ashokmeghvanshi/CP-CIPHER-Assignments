class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        
        l=[]
        currptr=head
        while currptr!=None:
            l.append(currptr.val)
            currptr=currptr.next
        
        
        NewHead = None
        
        for element in l:
            if NewHead==None and l.count(element) < 2:
                NewHead = ListNode(element)
                current = NewHead
            elif l.count(element) < 2:
                current.next = ListNode(element)
                current = current.next
        return NewHead
    
