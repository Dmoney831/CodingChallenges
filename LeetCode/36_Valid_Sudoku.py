def isValidSudoku(board): 
    rows = [{} for i in range(9)]
    cols = [{} for i in range(9)]
    boxes = [{} for i in range(9)]

    for i in range(9):
        for j in range(9):
            n = board[i][j]
            if n != '.':
                box_index = ((i//3) * 3) + (j//3)
                # print(box_index)
                rows[i][n] = rows[i].get(n, 0) + 1
                cols[j][n] = cols[j].get(n, 0) + 1
                boxes[box_index][n] = boxes[box_index].get(n, 0) + 1

                
                if rows[i][n] > 1 or cols[j][n] > 1 or boxes[box_index][n] > 1:
                    return False
    # print(rows)
    # print(cols)
    # print(boxes)
    return True


# if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
    
    


board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]


# board = [
#  ["7",".",".",".","4",".",".",".","."]
# ,[".",".",".","8","6","5",".",".","."]
# ,[".","1",".","2",".",".",".",".","."]
# ,[".",".",".",".",".","9",".",".","."]
# ,[".",".",".",".","5",".","5",".","."]
# ,[".",".",".",".",".",".",".",".","."]
# ,[".",".",".",".",".",".","2",".","."]
# ,[".",".",".",".",".",".",".",".","."]
# ,[".",".",".",".",".",".",".",".","."]
# ]

print(isValidSudoku(board))  

# var isValidSudoku = function(board) {
#     var map = {};
#     var temp = 0;
#     for (var i = 0; i < 9; i++) {
#       for (var j = 0; j < 9; j++) {
#         temp = board[i][j];
#         if (temp === '.') continue;
#         if (map['i' + i + temp] || map['j' + j + temp] || map['b' + Math.floor(i / 3) + Math.floor(j / 3) + temp]) return false;
#         map['i' + i + temp] = 1;
#         map['j' + j + temp] = 1;
#         map['b' + Math.floor(i / 3) + Math.floor(j / 3) + temp] = 1;
#         }
#     }
#     console.log(map)
#     return true;
# };