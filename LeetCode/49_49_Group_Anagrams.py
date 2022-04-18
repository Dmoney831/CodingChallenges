
def groupAnagrams(strs):
    g = {}
    for w in strs:
        x = "".join(sorted(w))
        # print(x)
        if x in g:
            g[x].append(w)
        else:
            g[x] = [w]
    print(list(g.values()))
    



strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)