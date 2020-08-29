class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def per(i,j,gird):

            if i<0 or j < 0 or i>=len(grid) or j >= len(grid[0]):

                return 0

            elif grid[i][j]==1:

                return 1

            return 0
        
        perimeter = 0

        R=len(grid)

        C=len(grid[0])

        for i in range(0,R):

            for j in range(0,C):

                if grid[i][j]==1:

                    c=0

                    c= per(i+1,j,grid)

                    c+=per(i,j+1,grid)

                    c+=per(i-1,j,grid)

                    c+=per(i,j-1,grid)

                    perimeter += (4-c)

        return perimeter
 
