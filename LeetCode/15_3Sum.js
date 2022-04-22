/**
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 * 
 */

var threeSum = function(nums) {
    var ans = [];
    nums = nums.sort((a,b) => a - b)

    for (let i = 0; i < nums.length; i++) {
        let num = nums[i]
        if (i > 0 && num == nums[i-1]){
            continue    
        }
        let l = i+1;
        let r = nums.length - 1;
        while (l < r) {
            sum = num + nums[l] + nums[r]
            if (sum > 0) {
                r--
            } else if (sum < 0) {
                l++
            } else {
                ans.push([num, nums[l], nums[r]])
                l++;
                while (nums[l] == nums[l - 1] && l < r) {
                    l++;
                }
            }
        }
    }
    console.log(ans)
}


var nums = [-1,0,1,2,-1,-4]
var output = [[-1,-1,2],[-1,0,1]]

threeSum(nums)

// Time Complexity: O(n^2)
// Space Complexity: O(1)