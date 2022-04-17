var removeElement = function(nums, val) {
    let z = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[z] = nums[i]
            z++
        }
    }
    return z
};