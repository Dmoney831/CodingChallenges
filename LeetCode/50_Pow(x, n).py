def myPow(x, n):
    if x >= 0:
        return x**n

x = 2.00000 
n = 10
# Output: 1024.00000


x = 2.10000 
n = 3
# Output: 9.26100


x = 2.00000 
n = -2
# Output: 0.25000

print(myPow(x, n))