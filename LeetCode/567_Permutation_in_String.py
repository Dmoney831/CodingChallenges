# Time Complexity: O(n)


def checkInclusion(s1, s2):
    long = len(s1)
    z = set(s1)
    x = {}

    for i in s1:
        x[i] = 1 + x.get(i,0)
    print(x)
    # print(s2[0:long])
    left = 0
    y = {}
    for right in s2:
        if right in z:
            y[right] = 1 + y.get(right, 0)
    print(y)
        




s1 = "ab" 
s2 = "eidbaooo"

# s1 = "ab" 
# s2 = "eidboaoo"

checkInclusion(s1, s2)