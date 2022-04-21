var isPalindrome = function(s) {
    s = s.toLowerCase();
    newS = ""
    
    var isLetter = function (char) {
        return (char >= 'a' && char <= 'z') || (char >= '0' && char <= '9');
    };

    for(let i of s) {
        if (isLetter(i)) {
            newS += i
        } 
    };
    revNewS = newS.split('').reverse().join('')

    return newS == revNewS
};



// var s = "A man, a plan, a canal: Panama"
var s = "race a car"
console.log(isPalindrome(s))
