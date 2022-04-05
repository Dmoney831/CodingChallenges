'''
1   1   1   1   1   1   1
1   2   3   4   5   6   7
1   3   6   10  15  21  28

'''
def uniquePaths(m,n):
    dp = [ [0]* n for _ in range(m) ]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

# Big 
'''
init the first row and first column that will cost O(m+n).
Then iterate all 2D dp array, it will cost O(m*n). 
In total will cost (m+n+mn), so generally, it's O(n^2).
'''