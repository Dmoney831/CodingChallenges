'''
You are climbing a staircase. It takes "n" steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Constraints: 1 <= n <= 45

Permutations 
n P r = (n!)/(n-r)!

Combinations
n C r = n! / (n-r)! / r!
'''

# def climbStairs(n):
    
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 3
#     elif n >= 4:
#         return climbStairs(n-1) + climbStairs(n-2)

def climbStairs(n):
    arr = [None,1,2]
    if n == 1:
        return arr[n]
    elif n == 2:
        return arr[2]
    elif n >= 3:
        for i in range(3, n+1):
            arr.append(arr[i-1]+arr[i-2])
    return arr[n]
        

# a = 2
a = 3
# a = 23
# print(climbStairs(a))