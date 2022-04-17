var strStr = function(haystack, needle) {
    if (haystack == null || needle == null) {
        return -1;
    }
    if (haystack == needle) {
        return 0;
    }
    var z = needle.length;
    for (let i = 0; i < haystack.length + 1 - z; i++) {
        if (haystack.substring(i, i + z) == needle){
            return i;
        }
    }
    return -1
    
};