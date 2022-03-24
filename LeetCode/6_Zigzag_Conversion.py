'''
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
'''

'''
top = 0, (numRow - 1)*2, (numRow - 1)*2
middle = 1, 1+(numRow) 
'''
def convert(s, numRows):
    if numRows == 1 :
        return s
    
    result = ""
    for r in range(numRows):
        increment = 2*(numRows-1)
        for i in range(r, len(s), increment):
            result += s[i]
            if (r > 0 and r < numRows - 1 and i + increment - 2*r < len(s)):
                result += s[i + increment - 2*r]
    return result



s = "PAYPALISHIRING" 
numRows = 3

# s = "PAYPALISHIRING" 
# numRows = 4

print(convert(s, numRows))