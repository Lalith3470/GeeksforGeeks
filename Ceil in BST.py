
class Solution:
    def findCeil(self,root, inp):
        # code here
        self.lst=[]
        def dfs(root,inp):
            if root.data>=inp:self.lst.append(root.data)
            if root.left:dfs(root.left)
            if root.right:dfs(root.right)
        dfs(root,inp)
        self.lst.sort()
        return self.lst[0]
