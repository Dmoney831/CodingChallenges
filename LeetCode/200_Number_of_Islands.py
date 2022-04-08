'''
Given an m*n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or veritically. You may assume all four edges of the grid are all surrounded by water.
'1' == land
'0' == water
all four edges of the grid is water. 
count only '1' which is connected verticallly or horizontally. 
if there diagnol position, count as one island. 
To find the number of island, we need to move from left top to bottom right. 
For each move we can go up or right or down or left directions. 
After each move, if we are out of the bondary or we find water or we repeat the path then we return to last move and change to another direction to move until we find 1 island. After we find island, we update the count and start to find another island. 
'''

def numIslands(grid):
    if not grid: return 0
    row = len(grid)
    col = len(grid)
    visited = set()
    count = 0
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    def findIsland(x,y):
        for dx, dy in directions:
            newX, newY = x+dx, y+dy
            if 0 <= newX <row and 0<=newY < col and grid[newX][newY] == '1' and (newX, newY) not in visited:
                visited.add((newX, newY))
                findIsland(newX, newY)
    for x in range(row):
        for y in range(col):
            if grid[x][y] == '1' and (x,y) not in visited:
                count += 1
                visited.add((x,y))
                findIsland(x,y)
    return count