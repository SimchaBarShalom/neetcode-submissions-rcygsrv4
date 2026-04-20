class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        islands=0
        rows=len(grid)
        cols=len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]!='1':
                return 
            grid[i][j]='#'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    islands+=1
                    dfs(i,j)
        return islands
        