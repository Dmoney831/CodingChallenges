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

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    hash = {}
    for i in s:
        if i not in hash:
            hash[i] = 1 + hash.get(i, 0)
        else: 
            hash[i] += 1

    for j in t:
        if j in hash:
            hash[j] -= 1
            if hash[j] == 0:
                del hash[j]
        
        else:
            return False

    return hash == {} 


s = "anagram" 
t = "nagaram"

print(isAnagram(s,t))

from collections import Counter

def are_anagrams(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

'''
Counter example =>
{ 'a':1, 'p':2, 'l':1, 'e':1 } 

'''