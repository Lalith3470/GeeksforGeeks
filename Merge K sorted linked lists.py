class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        # code here
        # return head of merged list
        lst=[]
        for i in arr:
            while i:
                lst.append(i.data)
                i=i.next
        a=Node(0)
        tmp=a
        lst.sort()
        for i in lst:
            tmp.next=Node(i)
            tmp=tmp.next
        return a.next
