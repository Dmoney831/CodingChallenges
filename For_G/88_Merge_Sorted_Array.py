def merge(nums1, m, nums2, n):
    
    for i in range(m, m+n):
        nums1[i] = nums2[i-m]
    nums1.sort()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

