
def findMedianSortedArrays(num1, num2):
    result = sorted(num1 + num2)
    # print(result)
    # print(len(result))
    if len(result) % 2 != 0:
        median_odd = int((len(result)-1)/2)
        # print(result[median_odd])
        return result[median_odd]
    if len(result) % 2 == 0:
        median_even = int((len(result)-2)/2)
        return (result[median_even] + result[median_even + 1])/2


a = [1,2,5,8]
b = [3,4,7,2]

def findMedianSortedArrays(num1, num2):
    sort = sorted(num1 + num2)
    mid = len(sort) // 2
    if len(sort) % 2 != 0:
        
        return sort[mid]
    if len(sort) % 2 == 0:
        
        return (sort[mid] + sort[mid] + 1) / 2


print(findMedianSortedArrays(a,b))