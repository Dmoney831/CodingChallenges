/**
 * Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 */
var topKFrequent = function(nums, k) {
    let map = new Map();
    for (let n of nums) {
        if(!map.has(n)) {
            map.set(n, 1);
        }
        else {
            map.set(n, map.get(n)+1);
        }
    };
    let x = [];
    for (let [key, value] of map) {
        x.push([key, value]);
    };
    x.sort(function(a,b) {
        return b[1] - a[1];
    });
    let z = [];
    for (let i = 0; i < k; i++) {
        z.push(x[i][0]);
    };
    return z
};