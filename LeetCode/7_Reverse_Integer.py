def reverse(x):
    if x > 0:
        a = str(x)
        # print(a)
        a1 = a[::-1]
        if int(a1) > 2**31 - 1:
            return 0
        else:
            return int(a1)
        
    if x < 0:
        a = str(x * -1)
        # print(a)
        a1 = a[::-1]
        if int(a1)*-1 < -2**31: 
            return 0
        else: 
            return int(a1)*-1

    if x == 0:
        return 0

    

# z = 123
z = -123
# z = 120

print(reverse(z))
print(reverse(-156384741))
print(reverse(156384741))
