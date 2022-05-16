def partitionLabels(s):
    lastIndex = {} # char -> last index in s

    for i, c in enumerate(s):
        lastIndex[c] = i
    print(lastIndex)    
    res = []
    size, end = 0, 0
    for i, c in enumerate(s):
        size += 1
        end = max(end, lastIndex[c])
        if i == end:
            res.append(size)
            size = 0
    return res


s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]

s = "eccbbbbdec"
# Output: [10]
print(partitionLabels(s))
# *****Time Complexity: O(n) since we traverse array.
# *****Space Complexity: O(1) saving in hash map with limited 26 characters.

