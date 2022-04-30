var findMin = function(nums){
    var l = 0, r = nums.length - 1

    while (l < r) {
        var mid = Math.floor((l + r) / 2)
        if (nums[mid] > nums[r]) {
            l = mid + 1
        } else {
            r = mid
        }
    }
    return nums[l]
}




a = [3,4,5,1,2]
b = [4,5,6,7,0,1,2]
c = [11,13,15,17]
console.log(findMin(a))
console.log(findMin(b))
console.log(findMin(c))