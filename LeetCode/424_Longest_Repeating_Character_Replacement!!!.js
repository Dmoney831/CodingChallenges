// O(26*n) => O(n)
var characterReplacement = function(s, k) {
    var char = {}
    var left = 0, max_freq = 0, result = 0;

    for (let right = 0; right < s.length; right++) {
        char[s[right]] = 1 + (char[s[right]] || 0)
        max_freq = Math.max(max_freq, char[s[right]])

        while( (right - left + 1) - max_freq > k ) {
            char[s[left]]--
            left++
        }
        result = Math.max(result, right - left + 1)
    }
    return result
}