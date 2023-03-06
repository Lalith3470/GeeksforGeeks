class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        lst=[]
        lst1=[]
        while head:
            if head.data<3:
                lst.append(head.data)
            else:
                lst1.append(head.data)
            head=head.next
        lst.sort()
        a=Node(0)
        tmp=a
        for i in lst+lst1:
            tmp.next=Node(i)
            tmp=tmp.next
        return a.next
