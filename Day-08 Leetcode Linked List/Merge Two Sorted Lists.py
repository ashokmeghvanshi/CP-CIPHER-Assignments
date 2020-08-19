
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        newlist = ListNode()

        newlistptr = newlist
        
        while l1 and l2:

            if l1.val <= l2.val:
                newlistptr.next = l1
                l1 = l1.next

            else:
                newlistptr.next = l2
                l2 = l2.next
            newlistptr = newlistptr.next

        if l1 != None:
            newlistptr.next = l1
        else:
            newlistptr.next = l2
            
        return newlist.next
        
        
