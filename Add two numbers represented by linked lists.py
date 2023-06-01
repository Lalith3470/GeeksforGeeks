class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        
        s1=""
        s2=""
        while first:
            s1+=str(first.data)
            first=first.next
        while second:
            s2+=str(second.data)
            second=second.next
        ans=str(int(s1)+int(s2))
        a=Node(0)
        tmp=a
        for i in ans:
            tmp.next=Node(int(i))
            tmp=tmp.next
        return a.next
