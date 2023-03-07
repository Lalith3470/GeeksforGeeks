You can also use the following for printing the link list.
printList(node)
"""

class Solution:
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        # code here
        lst=[]
        while head:
            lst.append(head.data)
            head=head.next
        lst[:k]=lst[:k][::-1]
        lst[k:]=lst[k:][::-1]
        a=Node(0)
        tmp=a
        for i in lst:
            tmp.next=Node(i)
            tmp=tmp.next
        return a.next

