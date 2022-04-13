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