class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0 or grid==None:
            return 0
        
        def countisland(i,j,gird):
            if i<0 or j < 0 or i>=len(grid) or j >= len(grid[0]) or grid[i][j]=='0':
                return 0
            grid[i][j]='0'
            countisland(i+1,j,grid)
            countisland(i-1,j,grid)
            countisland(i,j+1,grid)
            countisland(i,j-1,grid)
            return 1
        
        numofisland = 0
        R=len(grid)
        C=len(grid[0])
        for i in range(0,R):
            for j in range(0,C):
                if grid[i][j]=='1':
                    numofisland+=countisland(i,j,grid)
                    
        return numofisland
 
