'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are gien an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r,c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height i less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean. 


'''
def pacific_atlantic(matrix):
    # if not matrix or not matrix[0]: return []
    # print(matrix[0])
    m,n = len(matrix), len(matrix[0])
    p_visited = set()
    a_visited = set()
    directions = [(-1, 0), (0, -1),  (1, 0), (0, 1)]
    def dfs(visited, x,y):
        visited.add((x,y))
        # print(visited)
        for dx, dy in directions: 
            new_x, new_y = x+dx, y+dy
            print(f"x: {x}, y: {y}, dx: {dx}, dy: {dy}, new_x: {new_x}, new_y: {new_y}, visited: {(visited)}")
            if 0 <= new_x < m and 0 <=new_y < n and (new_x, new_y) not in visited and matrix[new_x][new_y] >=matrix[x][y]:
                dfs(visited, new_x, new_y)

    for i in range(m):
        dfs(p_visited, i, 0)
        dfs(a_visited, i, n-1)
    for j in range(n):
        dfs(p_visited, 0, j)
        dfs(a_visited, m-1, j)
    return list(p_visited.intersection(a_visited))


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# heights = [[2,1],[1,2]]
# heights = [[1,2,3],[2,1,3],[3,1,2]]

print(pacific_atlantic(heights))


'''
time complexity is O(2mn)
'''

# def abc(x):
#     for i,j in x:
#         print(i,j)
# abc([(1,0), (2,0), (3,0)])