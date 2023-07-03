#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        while head != None:
            if head.data == -1:
                return True
            head.data = -1
            head = head.next
        return False
