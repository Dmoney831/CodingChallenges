var minEatingSpeed = function(piles, h) {
    var l = 1, r = Math.max(...piles)
    var result = r
    
    while (l <= r) {
      var k = Math.floor(l + r) / 2
      var hours = 0
      for (let p of piles) {
        hours += (p / k)
        // console.log(hours)
      }
      if (hours <= h) {
        result = Math.min(result, k)
        r = k - 1
      } else {
        l = k + 1
      }
    }
  return k
};



var piles = [3,6,7,11], h = 8
// var piles = [30,11,23,4,20], h = 5
// var piles = [30,11,23,4,20], h = 6

console.log(minEatingSpeed(piles, h))