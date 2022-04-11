######Fibonacci#####
def fib(n):
    ans = [0 for i in range(n+1)]
    ans[1], ans[2] = 1, 1

    for i in range(3, n+1):
        ans[i] = ans[i-1] + ans[i-2]
        # print(ans[i-2])

    print(ans[n])
    
fib(8)
# fib(50)

######Travel Grid#######
def gridTraveler(row, col):
    if row == 0 or col == 0:
        return 0
    # if row == 1 or col == 1:
    #     return 1
    arr = [ [ 1 for c in range(col)] for r in range(row)]
    arr[0][0] = 0
    # print(arr)
    for i in range(1, row):
        for j in range(1, col):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(arr[row-1][col-1])


'''
*****Brute Force***** 
=> Time Complexity = O(2^(m*n))
=> Space Complexity = O(m+n)

*****Memoized*******
=> Time complexity = O(m * n)
=> Space complexity = O(n + m)

'''
gridTraveler(3,3)
# gridTraveler(18,18)






