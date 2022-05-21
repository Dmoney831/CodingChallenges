def generate(numRows):
    res = []
    for i in range(numRows):
        res.append([1]*(i+1))
        # print(res)
        if i > 1:
            for j in range(1, i):
                # print(res[i][j], res[i-1][j-1], res[i-1][j])
                # print(i,j, i-1,j-1, i-1,j ) 
                res[i][j] = res[i-1][j-1] + res[i-1][j]
                # print(res)
    return res
numRows = 5
generate(numRows)