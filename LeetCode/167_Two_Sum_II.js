var twoSum = function(numbers, target) {
    var hash = {};
    for (let i = 0; i < numbers.length; i++) {
        let num = numbers[i];
        let diff = target - num
        if (hash[diff] !== undefined) {
            return [hash[diff]+1, i+1]
        } else {
            hash[num] = i
        }
    }
    
};

var numbers = [2,7,11,15]
var target = 9

console.log(twoSum(numbers, target))

// Time complexity: O(n)
// Space Complexity: O(n)

