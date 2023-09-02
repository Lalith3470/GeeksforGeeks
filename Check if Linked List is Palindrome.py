class Solution:
    def isPalindrome(self, head):
        
        #code here
        lst=[]
        while head:
            lst.append(head.data)
            head=head.next
        return lst==lst[::-1]
