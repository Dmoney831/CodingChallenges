var isPalindrome = function(x) {
    return x == x.toString().split('').reverse().join('')
};

var isPalindrome = function(x) {
    if (x < 0) {
        return false
    }
    var z = x
    let rev = 0
    while (x>0) {
        rev = rev*10 + (x%10);
        x = parseInt(x/10);
    }
    return z == rev
}
x = 12321
// Output: true


console.log(isPalindrome(x))
