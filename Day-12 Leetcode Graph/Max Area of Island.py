class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid)==0 or grid==None:
            return 0
        
        def maxareaisland(i,j,gird):
            if i >=0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j]==1:

                grid[i][j]=0
                return 1+maxareaisland(i+1,j,grid)+maxareaisland(i-1,j,grid)+maxareaisland(i,j+1,grid)+maxareaisland(i,j-1,grid)
            return 0
        
        maxarea = 0
        R=len(grid)
        C=len(grid[0])
        for i in range(0,R):
            for j in range(0,C):
                if grid[i][j]==1:
                    maxarea=max(maxarea,maxareaisland(i,j,grid))
                    
        return maxarea
 
