def fib(n):
    
    ans = [0 for i in range(n+1)]
    # print(ans)
    ans[1], ans[2] = 1, 1

    for i in range(3, n+1):
        ans[i] = ans[i-1] + ans[i-2]
        # print(ans[i-2])

    print(ans[n])
    
fib(3)
fib(4)
fib(5)
fib(6)
fib(7)
fib(8)
fib(50)