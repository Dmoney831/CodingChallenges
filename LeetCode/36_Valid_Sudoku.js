/**
 * 9 X 9 Sudoku board.
 * Number.isInteger(value)
 */

var isValidSudoku = function(board) {
    var map = {};
    var temp = 0;
    for (var i = 0; i < 9; i++) {
      for (var j = 0; j < 9; j++) {
        temp = board[i][j];
        if (temp === '.') continue;
        if (map['i' + i + temp] || map['j' + j + temp] || map['b' + Math.floor(i / 3) + Math.floor(j / 3) + temp]) return false;
        map['i' + i + temp] = 1;
        map['j' + j + temp] = 1;
        map['b' + Math.floor(i / 3) + Math.floor(j / 3) + temp] = 1;
        }
    }
    console.log(map)
    return true;
};

// Time Complexity: O(n^2)
// Space Complexity: O(n)



// var board = 
// [["5","3",".",".","7",".",".",".","."]
// ,["6",".",".","1","9","5",".",".","."]
// ,[".","9","8",".",".",".",".","6","."]
// ,["8",".",".",".","6",".",".",".","3"]
// ,["4",".",".","8",".","3",".",".","1"]
// ,["7",".",".",".","2",".",".",".","6"]
// ,[".","6",".",".",".",".","2","8","."]
// ,[".",".",".","4","1","9",".",".","5"]
// ,[".",".",".",".","8",".",".","7","9"]]

var board =
[["7",".",".",".","4",".",".",".","."]
,[".",".",".","8","6","5",".",".","."]
,[".","1",".","2",".",".",".",".","."]
,[".",".",".",".",".","9",".",".","."]
,[".",".",".",".","5",".","5",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".","2",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]]

console.log(isValidSudoku(board))