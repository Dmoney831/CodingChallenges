def countAndSay(n):
    s = '1'
    for _ in range(n-1):
        say = s[0]
        temp = ''
        count = 0
        for left in s:
            if say == left:
                count += 1
            else:
                temp += str(count) + say
                say = left
                count = 1
        temp += str(count) + say
        s = temp
    return s
        


n = 4
'''
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 one 1 = "1211"

'''
print(countAndSay(n))
