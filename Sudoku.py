
class Solution:
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        def solve(grid):
            def valid(grid,i,j,c):
                for k in range(9):
                    if grid[k][j]==c:return False
                    if grid[i][k]==c:return False
                    if grid[3*(i//3)+k//3][3*(j//3)+k%3]==c:return False
                return True
            for i in range(9):
                for j in range(9):
                    if(grid[i][j]==0):
                        for c in range(9):
                            if(valid(grid,i,j,c+1)):
                                grid[i][j]=c+1
                                if(solve(grid)==True):
                                    return True
                                else:
                                    grid[i][j]=0
                        return False
            return True
                                
        return solve(grid)
        
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        # Your code here
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=" ")
