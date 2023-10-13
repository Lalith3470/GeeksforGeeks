class Solution:
    def floor(self, root, x):
        curr=root
        result=-1
        while curr:
            if curr.data==x:
                return x
            elif curr.data>x:
                curr=curr.left
            else:
                result=curr.data
                curr=curr.right
        return result
