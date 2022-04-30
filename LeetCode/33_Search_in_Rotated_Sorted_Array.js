var search = function(nums, target) {
    var l = 0, r = nums.length - 1;
    while (l <= r) {
      var mid = Math.floor((l+r)/2)
      if (target === nums[mid]) {
        return mid
      }
      if (nums[l] <= nums[mid]) {
        if (target > nums[mid] || target < nums[l]) {
          l = mid + 1
        } else {
          r = mid - 1
        }
      } else {
        if (target < nums[mid] || target > nums[r]) {
          r = mid - 1
        } else {
          l = mid + 1
        }
      }
    }
    return - 1
};
var nums = [4,5,6,7,0,1,2], target = 0
search(nums, target)