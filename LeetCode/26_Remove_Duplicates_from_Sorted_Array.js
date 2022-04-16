/*
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

*/


// var removeDuplicates = function(nums) {
//     var res = []
//     var nums = nums.sort()
//     // var x = new Set(nums);
//     var x = [...new Set(nums)];
//     var extraLen = new Array(nums.length - x.length).fill('_');
//     var x = x.concat(extraLen)
//     console.log(extraLen)
//     console.log(x.length, x)
// }

var removeDuplicates = function(nums) {
    var len = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i-1] != nums[i]) {
            nums[len] = nums[i];
            len++
        }
            
    } return len;
    
};

nums = [3,1,1,2]
// Output= 2, nums = [1,2,_]

removeDuplicates(nums)