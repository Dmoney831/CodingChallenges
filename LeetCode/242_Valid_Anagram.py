def isAnagram(s,t):
    ss, tt = len(s), len(t)
    if ss != tt :
        return False
    d1 = {}
    d2 = {}
    for i in s:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in t:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
    for key in d1:
        if key not in d2 or d1[key] != d2[key]:
            return False
    return True

from collections import Counter

def are_anagrams(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

'''
Counter example =>
{ 'a':1, 'p':2, 'l':1, 'e':1 } 

'''