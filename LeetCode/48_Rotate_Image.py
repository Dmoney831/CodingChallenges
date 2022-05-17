def rotate(matrix):
    n = len(matrix)
    # swap diagonal way
    for i in range(n):
        for j in range(n):
            if i < j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # and reverse each rows.
    for x in matrix:
        x.reverse()
    return matrix
    
      


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

print(rotate(matrix))

# Time Complexity: O(n^2)
# Space Complexity: O(n)