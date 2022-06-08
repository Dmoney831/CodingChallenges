class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # nums are in descending order
        i = j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        # find the last "ascending" position
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        # reverse the second part
        left, right = k+1 , len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        

        


nums = [5,4,3,2,1]
# out -> [1,2,3,4,5]

nums = [1,2,7,9,6,4,1]
# out -> [1,2,9,1,4,6,7]
nums = [1,2,9,9,8,3]
# out -> [1,8,3,7,9,9]