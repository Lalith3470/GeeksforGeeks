from collections import deque
#Function to find the lowest common ancestor in a BST. 
def LCA(root, n1, n2):
    #code here.
    if (n1<root.data) and (n2<root.data):
        return LCA(root.left,n1,n2)
    if (n1>root.data) and (n2>root.data):
        return LCA(root.right,n1,n2)
    return root
