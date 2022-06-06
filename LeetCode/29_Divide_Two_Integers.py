import math
def divide(dividend, divisor):
    q = dividend // divisor
    qq = dividend / divisor
    if q < 0:
        return math.ceil(qq) if math.ceil(qq) > -2**31 else -2**31
    if q >= 0:
        return q if q <= 2**31 - 1 else 2*831 - 1
        

dividend, divisor = 7, -3
print(divide(dividend, divisor))