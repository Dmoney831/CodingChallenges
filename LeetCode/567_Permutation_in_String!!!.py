# Time Complexity: O(n)

def checkInclusion(s1, s2):
    x = {}
    s3 = s2 
    print(s3)

    for i in s1:
        x[i] = 1 + x.get(i,0)
    print(x)
    # print(s3[0:long])
    left = 0
    y = {}
    for i in range(len(s3)):
        y[s3[i]] = 1 + y.get(s3[i], 0)
        print(y)
        if s3[i] not in s1:
            y.pop(s3[i-1])
            print(y)
            # del y[s3[i-1]]
    
    print(x == y)
        
from collections import Counter
def checkInclusion(s1, s2):
    cntr, w = Counter(s1), len(s1)
    print(cntr)
    for i in range(len(s2)):
        if s2[i] in cntr:
            cntr[s2[i]] -= 1
            print(cntr)
        if i >= w and s2[i-w] in cntr:
            cntr[s2[i-w]] += 1
            print(cntr)
        if all([cntr[i] == 0 for i in cntr]):
            return True
    return False
        


s1 = "ab" 
s2 = "eidbaooo"

s1 = "ab" 
s2 = "eidboao"

print(checkInclusion(s1, s2))