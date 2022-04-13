var longestCommonPrefix = function(s) {
    s.sort();
    z = s.length;
    min_l = Math.min(s[0].length, s[z-1].length)
    // console.log(s)
    // console.log(min_l)
    left = 0
    while (left < min_l && s[0][left] == s[z-1][left]){
        left += 1
    }
    prefix = s[0].slice(0, left);
    console.log(prefix)




}

s = ["flower","flow","flight"]
// s = ["dog","racecar","car"]
longestCommonPrefix(s)