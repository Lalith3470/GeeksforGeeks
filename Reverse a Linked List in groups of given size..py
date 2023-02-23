"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        # Code here
        lst=[]
        while head:
            lst.append(head.data)
            head=head.next
        lst1=[]
        for i in range(0,len(lst),k):
            lst1+=(lst[i:i+k])[::-1]
        a=Node(0)
        tmp=a
        for i in lst1:
            tmp.next=Node(i)
            tmp=tmp.next
        return a.next
