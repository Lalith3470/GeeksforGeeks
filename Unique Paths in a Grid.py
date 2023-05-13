class Solution:
    def uniquePaths(self, n, m, grid):
        # code here 
        dp=grid
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    continue
                if grid[i][j]==0:
                    continue
                else:
                    up=0
                    down=0
                    if i>0:up=dp[i-1][j]
                    if j>0:down=dp[i][j-1]
                    dp[i][j]=up+down
        return dp[-1][-1]%(10**9+7)
