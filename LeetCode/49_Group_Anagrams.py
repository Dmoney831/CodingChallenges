
def groupAnagrams(strs):
    g = {}
    for w in strs:
        x = "".join(sorted(w))
        # print(sorted(w))
        if x in g:
            g[x].append(w)
        else:
            g[x] = [w]
    print(g.values())
    print(list(g.values()))
    



strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)