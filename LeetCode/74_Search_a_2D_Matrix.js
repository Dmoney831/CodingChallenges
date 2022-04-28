var searchMatrix = function(matrix, target) {
    for (i in matrix) {
      if (matrix[i].includes(target)) {
        return true
      }
    }
  return false
}

var matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// var matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13

searchMatrix(matrix, target)