def setZeroes(matrix):
    row = len(matrix)
    col = len(matrix[0])

    first_row_has_zero = False
    first_col_has_zero = False
    # iterate through matrix to mark the zero row and col
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 0:
                if r == 0:
                    first_row_has_zero = True
                if c == 0:
                    first_col_has_zero = True
                elif r != 0 and c != 0: 
                    matrix[r][0] = matrix[0][c] = 0
    print(matrix)
    # iterate through matrix to update the cell to be zero if it's in a zero row or col
    for r in range(1, row):
        for c in range(1, col):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] == 0
    
    # update the first row and col if they're zero
    if first_row_has_zero:
        for c in range(col):
            matrix[0][c] == 0
    if first_col_has_zero:
        for r in range(row):
            matrix[r][0] == 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

print(setZeroes(matrix))

#**** Time Complexity: O(m*n) since we loop through the 2D matrix.
# **Space Complexity: O(1)