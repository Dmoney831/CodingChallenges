var lengthOfLongestSubstring = function(s) {
    // var xSet = [...new Set(s)]
    // console.log(xSet)
    var char = [];
    var num = [];
    var count = 0;
    if (s.length < 2) {
        return s.length
    }

    for (let i = 0; i < s.length; i++) {
        if (!char.includes(s[i])) {
            char.push(s[i])
            count++
            num.push(count)
        } else {
            x = char.indexOf(s[i])
            console.log(x)
            char.push(s[i])
            char.splice(0, x+1)
            console.log(char)
            count = count - x 
        }
    }
    console.log(char)
    console.log(Math.max(...num))

};

var lengthOfLongestSubstring = function(s) {
    var set = new Set();
    var left = 0;
    var result = 0;
    for (right in s) {
        while (set.has(s[right])) {
            set.delete(s[left])
            left++
        }
        set.add(s[right])
        result = Math.max(result, right - left + 1)
    }
    console.log(result)
};

var s = "abcabcbb"
// var s = "au"
// var s = "pwwkew"
// var s = "dvdf"
// var s = "xdvidfveo"
lengthOfLongestSubstring(s)
