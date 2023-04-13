class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        dic={}
        v=Node(1)
        tmp=v
        while head:
            a=head.data
            if a not in dic:
                dic[a]=1
                tmp.next=Node(a)
                tmp=tmp.next
            head=head.next
        return v.next
