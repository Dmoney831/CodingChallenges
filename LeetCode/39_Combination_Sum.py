'''
iterate over the candiates value and append candidates[i].
same value can be used unlimited.
backtracking + combination
'''


def combinationSum(candidates, target):
    res = []
    
    def depth_for_search(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        depth_for_search(i, cur, total + candidates[i])
        cur.pop()
        depth_for_search(i+1, cur, total)

    depth_for_search(0, [], 0)
    return res

    


def combinationSum(candidates, target):
    res = []
    candidates.sort()

    def dfs(cur, path):
        if cur == 0:
            res.append(path)
        for n in candidates:
            if n > cur:
                break
            if path and n < path[-1]:
                continue
            dfs(cur - n, path + [n])
    dfs(target, [])
    return res


candidates = [2,3,6,7] 
target = 7
candidates = [2,3,5] 
target = 8
candidates = [2] 
target = 1
