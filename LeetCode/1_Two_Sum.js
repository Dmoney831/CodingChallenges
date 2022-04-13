var twoSum = function(nums, target) {
    var map = {};
    for (var i = 0; i < nums.length; i++) {
        var num = nums[i];
        var diff = target - num;
        if (map[diff] !== undefined) {
            return [map[diff], i];
        } else {
            map[num] = i;
        }
    }
};
nums = [1,2,3,4,5]
target = 9
console.log(twoSum(nums, target))


// nums = [1,2,3,4,5]
// hash(nums)