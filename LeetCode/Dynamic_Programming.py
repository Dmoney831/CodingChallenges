'''
######Memoization Recipe############
# 1. Make it work.
=> visualize the problem as a tree
=> implement the tree using recursion
=> test it 
=> 

# 2. Make it efficient.
=> use created empty or default value array
=> add a base case to return array value
=> store return values into the array

'''


######Fibonacci#####
def fib(n):
    ans = [0 for i in range(n+1)]
    ans[1], ans[2] = 1, 1

    for i in range(3, n+1):
        ans[i] = ans[i-1] + ans[i-2]
        # print(ans[i-2])

    print(ans[n])
    
# fib(8)
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
# gridTraveler(3,3)
# gridTraveler(18,18)




#####canSum#####

'''
Write a function 'canSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed. 
You may assume that all input numbers are non-negative.

canSum(7, [5, 3, 4, 7]) => True
canSum(7, [2,4]) => False

'''
def canSum(target, nums):
    if target == 0: return True
    if target < 0: return False
    
    for i in range(len(nums)):
        r = target - nums[i]
        if canSum(r, nums) == True:
            return True
    return False


'''
n = target sum
m = array length

Time Complexity =>
O(n^m) 
Space Complexity =>
O(m) 
'''
def canSum(target, nums):
    if target == 0: return True
    if target < 0: return False
    m = len(nums)
    n = target 

    table = [ 0 for k in range(n+1)]
    table[0] = 1
    for i in range(m):
        for j in range(nums[i], n+1):
            table[j] += table[j - nums[i]]
            # print(f'table[j]: {table[j]}, [j-nums[i]]: {j-nums[i]}, table[j - nums[i]]: {table[j - nums[i]]}, nums[i]: {nums[i]} ')
    # print(table)
    return table[n] != 0

'''
Time Complexity =>
O(n*m)
Space Complexity =>
O(m)
'''    
    


print(canSum(7, [2,3]))
# print(canSum(7, [5, 3, 4, 7]))
# print(canSum(7, [2, 4]))
# print(canSum(8, [2, 3, 5]))
# print(canSum(300, [7,14]))

'''
Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing any combination of elements that add up to exactly the targetSum. If there's no combination that adds up to the targetSum, then return null.

If there are multiple combinations possible, you may return any single one.

howSum(7, [5, 3, 4, 7]) => [3,4] or [7]
howSum(8, [2, 3, 5]) => [2, 2, 2, 2] or [3,5]
howSum(7, [2,4]) => null
'''