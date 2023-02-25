class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        lst=[]
        while head:
            lst.append(head.data)
            head=head.next
        lst=lst[::-1]
        head=Node(0)
        tmp=head
        for i in lst:
            tmp.next=Node(i)
            tmp=tmp.next
        return head.next
