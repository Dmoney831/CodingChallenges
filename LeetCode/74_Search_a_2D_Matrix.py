def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        if target in matrix[i]:
            return True
    return False



def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    top, bottom = 0, m - 1
    while top <= bottom:
        row = (top + bottom) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break
    # if target is not in any rows in while loop
    if not (top <= bottom):
        return False
    
    # check target in a specific row
    row = (top + bottom) // 2
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if target > matrix[row][mid]:
            left = mid + 1
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            return True
    return False





matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3
print(searchMatrix(matrix, target))