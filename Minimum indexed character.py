class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        val=curr_node.next.data
        curr_node.data=val
        curr_node.next=curr_node.next.next
