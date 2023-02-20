class Solution:
    def reverseBetween(self, head, m, n):
        #code here
        lst=[]
        while head:
            lst.append(head.data)
            head=head.next
        lst=lst[:m-1]+(lst[m-1:n])[::-1]+lst[n:]
        a=Node(0)
        tmp=a
        for i in lst:
            tmp.next=Node(i)
            tmp=tmp.next
        return a.next
