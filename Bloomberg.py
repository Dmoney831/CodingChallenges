array = [1,2,3,4,1,3,2,4,2,3,1,3,5]
# => [5,4,4,1,1,1,2,2,2,3,3,3,3]

def sorting(array):
    hash = {}
    array.sort()
    for i in array:
        hash[i] = hash.get(i, 0) + 1
    
    res = []
    hash = {k: v for k, v in sorted(hash.items(), key=lambda item: item[1])}
    print(hash)
    
    for i in hash:
        for _ in range(hash[i]):
            res.append(i)
        
    return res

print(sorting(array))