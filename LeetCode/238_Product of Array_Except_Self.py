# def productExceptSelf(nums):
#     result = [1]*(len(nums))
#     prefix = 1
#     for i in range(len(nums)):
#         result[i] = prefix
#         prefix *= nums[i]
#         print(f'index: {i}, result[{i}]: {result[i]} prefix: {prefix}')
#         print(result)
#         print('')
#     postfix = 1
#     for i in range(len(nums)-1, -1 , -1):
#         result[i] *= postfix
#         postfix *= nums[i]
#         print(f'index: {i}, result[{i}]: {result[i]} postfix: {postfix}')
#         print(result)
#         print('')
        
def productExceptSelf(nums):
    result = [1]*len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1, -1 ,-1):
        result[i] *= postfix
        postfix *= nums[i]
    print(result)
        

        



# a = [1,2,3,4]
# a = [1,2,3,4,5,6]
a = [-1, 1, 0, -3, 3]
productExceptSelf(a)
# a.remove(a[1])
# print(a)
# print(a[2:] + a[0::-1])
# print(a[1:len(a)])
# print(a[2:]+ a[0::-1])
# print(a[1:]+ a[-1::-1])
