class Solution:
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        # code here
        dic={}
        ans=[]
        def dfs(root):
            if root.data in dic:ans.append(root.data)
            if root.left==None and root.right==None:
                return
            if root.left:dfs(root.left)
            if root.right:dfs(root.right)
        def dfs1(root):
            if root.data not in dic:
                dic[root.data]=1
            if root.left==None and root.right==None:
                return
            if root.left:dfs1(root.left)
            if root.right:dfs1(root.right)
        dfs1(root1)
        dfs(root2)
        return sorted(ans)
