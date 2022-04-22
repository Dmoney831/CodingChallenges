/**
 * prices = [ 7,1,5,3,6,4]
 * Output: 5
 * 
 */

var maxProfit = function(prices) {
    var big = 0;
    var i = 0;
    var j = 1;
    while (j < prices.length) {
        profit = prices[j] - prices[i]
        if (prices[i] < prices[j]) {
            big = Math.max(profit, big)
        } else {
            i = j
        }
        j++
    }
    return big
};


var prices = [ 7,1,5,3,6,4]
// console.log(Math.max(prices))
maxProfit(prices)
