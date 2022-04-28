var search = function(nums, target) {
    nums = nums.sort(function(a, b) {return a - b})
    var l = 0, r = nums.length - 1;

    while (l <= r) {
        m = parseInt((l+r)/2)
        if (nums[m] < target) {
            l = m + 1
        } else if (nums[m] > target) {
            r = m - 1
        } else {
            return m
        }
    }
    return -1
}


var nums = [-1,0,3,5,9,12], target = 9
console.log(search(nums, target))