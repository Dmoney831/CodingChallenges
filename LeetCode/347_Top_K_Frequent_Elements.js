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

var topKFrequent = function(nums, k) {
    let map = {};
    for (let i of nums) {
      console.log(i)
      if (!map[i]) {
        map[i] = 1
      } 
      else {
        map[i] += 1
      }
    };
  console.log(map)
  let objArr = Object.keys(map).sort((a,b) => map[b] - map[a]);
  console.log(objArr);
  return objArr.slice(0,k).map(i => Number(i))
};