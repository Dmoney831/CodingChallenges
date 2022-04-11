######Fibonacci#####
def fib(n):
    ans = [0 for i in range(n+1)]
    ans[1], ans[2] = 1, 1

    for i in range(3, n+1):
        ans[i] = ans[i-1] + ans[i-2]
        # print(ans[i-2])

    print(ans[n])
    
fib(50)

'''
gridTraveler(grid):

'''