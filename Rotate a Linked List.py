

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        lst=[]
        while head:
            lst.append(head.data)
            head=head.next
        for i in range(k):
            lst=lst[1:]+[lst[0]]
        a=Node(0)
        tmp=a
        for i in lst:
            tmp.next=Node(i)
            tmp=tmp.next
        return a.next
