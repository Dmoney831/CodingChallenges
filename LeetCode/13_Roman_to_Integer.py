def romanToInt(s):
    
    dict = { "I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
    
    output = 0
    for i in s:
        output += dict[i]
        
    l, r = 1, len(s)-1
    minusOne = 0
    minusTen = 0
    minusHun = 0
    while l <= r:
        if (s[l-1] == "I" and s[l] == "V") or (s[l-1] == "I" and s[l] == "X"):
            minusOne += 2        
        elif (s[l-1] == "X" and s[l] == "L") or (s[l-1] == "X" and s[l] == "C"):
            minusTen += 2    
        elif (s[l-1] == "C" and s[l] == "D") or (s[l-1] == "C" and s[l] == "M"):
            minusHun += 2
        l += 1
    
    print(output)
    print(minusOne, minusTen, minusHun)
    print(output - (minusOne) - (minusTen*10) - (minusHun*100))



# s = "III"
# Output: 3

# s = "LVIII"
# Output: 58

s = "MCMXCIV"
# Output: 1994

romanToInt(s)