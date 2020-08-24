class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        a,b='',''
        
        while l1!=None:

            a=a+str(l1.val)

            l1=l1.next

        while l2!=None:

            b=b+str(l2.val)

            l2=l2.next

        a=a[::-1]

        b=b[::-1]

        s=int(a)+int(b)

        s=str(s)[::-1]

        l3=ListNode()

        temp=l3

        for i in range(len(s)):

            temp.val=int(s[i])

            if i!=len(s)-1:

                temp.next=ListNode()

                temp=temp.next
            
        return l3
