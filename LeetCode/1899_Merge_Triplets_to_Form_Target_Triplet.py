def mergeTriplets(triplets, target):
    # if there are two arrays inside the master array merge first and last.
    # if there 4 or more merget first and third arrays and merge with last array. 
    forbidden = set()
    for i, [x, y, z] in enumerate(triplets):
        if x > target[0] or y > target[1] or z > target[2]:
            forbidden.add(i)
    a, b, c = 0, 0, 0
    for i, (x, y, z) in enumerate(triplets):
        if i not in forbidden:
            a, b, c = max(a, x), max(b, y), max(c, z)
    return [a ,b ,c] == target
    

    # (0,2)
    # (0,2,3)
    # (0,2,)

triplets = [[2,5,3],[1,8,4],[1,7,5]] 
target = [2,7,5]
# Output: true
triplets = [[3,4,5],[4,5,6]] 
target = [3,2,5]
# Output: false
triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]] 
target = [5,5,5]
# Output: true

print(mergeTriplets(triplets, target))

# ******time Complexity: O(n)
# ******space Complexity: O(n)
