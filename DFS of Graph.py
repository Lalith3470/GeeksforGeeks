
class Solution:
    #Function to return a list containing the DFS traversal of the graph.
        
    def dfsOfGraph(self, V, adj):
        # code here
        lst=[]
        def dfs(st):
            if st not in lst:
                lst.append(st)
                for i in adj[st]:
                    dfs(i)
        dfs(0)
        return lst
