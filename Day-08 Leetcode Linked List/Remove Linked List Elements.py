class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while head and head.val == val:

            head = head.next

        if head !=None:

            prevptr, curptr = head, head.next

            while curptr!=None:

                if curptr.val == val:

                    prevptr.next = curptr.next

                else:

                    prevptr = prevptr.next

                curptr = curptr.next

        return head
