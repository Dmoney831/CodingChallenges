/**
 * Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 */
var topKFrequent = function(nums, k) {
    let map = new Map();
    for (let n of nums) {
        if(!map.has(n)) {
            map.set(n, 1)
        }
        else {
            map.set(n, map.get(n)+1)
        }
    };
    let sorting = [];
    for (let [key, value] of map) {
        sorting.push([key, value])
    };
    sorting.sort(function(a,b) {
        return b[1] - a[1]
    });
    let answer = [];
    for (let i = 0; i < k; i++) {
        answer.push(sorting[i][0])
    };
    return answer
};