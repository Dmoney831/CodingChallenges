/**
 * Input: nums = [1,2,3,4]
 * Output: [24,12,8,6]
 * 
 * Input: nums = [-1,1,0,-3,3]
 * Output: [0,0,9,0,0]
 * 
 */

var productExceptSelf = function(nums) {
    var arr = Array(nums.length).fill(1)
    console.log(arr)
    var prefix = 1;

    for(let i = 0; i < nums.length; i++) {
        arr[i] = prefix;
        prefix *= nums[i];
    };
    var post = 1
    for (let i = nums.length-1; i >= 0; i--) {
        arr[i] *= post;
        post *= nums[i]
    };
    console.log(arr)
};


const nums = [1,2,3,4]
productExceptSelf(nums)