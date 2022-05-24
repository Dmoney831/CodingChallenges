def Integer_to_Roman(num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res, i = "", 0
    while num:
        res += (num//values[i]) * numerals[i]
        num = num % values[i]
        i += 1
    return res

num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.


num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

num = 497
# Output: "CDXCVII"

num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

num = 3212

print(Integer_to_Roman(num))