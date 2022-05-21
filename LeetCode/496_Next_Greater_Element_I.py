def nextGreaterElement(nums1, nums2):
    dct = {}
    stack = []

    for n in nums2:
        while stack and n > stack[-1]:
            dct[stack.pop()] = n
        stack.append(n)
    print(dct)
    return [dct.get(n, -1) for n in nums1]


    



nums1 = [4,1,2] 
nums2 = [1,3,4,2]
# Output: [-1,3,-1]
nums1 = [3,1,2,4] 
nums2 = [1,3,5,4,2]
# Output: [5,3,-1,-1]
print(nextGreaterElement(nums1, nums2))