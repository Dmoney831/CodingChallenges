def getRow(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0]+row, row+[0])]
        print(row)
    return row
def getRow(rowIndex):
    pascal = [1]*(rowIndex+1)
    for i in range(2, rowIndex + 1):
        for j in range(i-1, 0, -1):
            pascal[j] += pascal[j-1]
    return pascal



rowIndex = 4
print(getRow(rowIndex))

