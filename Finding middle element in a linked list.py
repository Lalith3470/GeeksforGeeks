# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        lst=[]
        cnt=0
        while head:
            lst.append(head.data)
            head=head.next
            cnt+=0.5
        return lst[int(cnt)]
