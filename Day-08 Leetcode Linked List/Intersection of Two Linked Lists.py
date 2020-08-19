class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cA = 0
        cB = 0
        newA = headA
        newB = headB
        
        while newA:
            cA += 1
            newA = newA.next
        while newB:
            cB += 1
            newB= newB.next 
        
        d = cA - cB
        if d < 0:
            c = 0
            while c < abs(d):
                c += 1
                headB = headB.next 
        elif d > 0:
            c = 0 
            while c < d:
                c += 1 
                headA = headA.next 

        while headA  and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return  None
