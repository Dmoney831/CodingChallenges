// var s = { a: 3, g: 1, m: 1, n: 1, r: 1 }
// var t = { a: 3, g: 1, m: 1, n: 1, r: 1 }

// console.log(JSON.stringify(s) === JSON.stringify(t))

var isAnagram = function(s, t) {
    var ss = s.length;
    var tt = t.length;
    if (ss != tt) {
        return false;
    };
    
    var d1 = {};
    var d2 = {};
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] in d1) {
            d1[s[i]]++;
        }
        else {
            d1[s[i]]=1;
        }
    };
    for (let i = 0; i < t.length; i++) {
        if (t[i] in d2) {
            d2[t[i]]++;            
        }
        else {
            d2[t[i]] = 1;
        }
    };
    var newD1 = Object.keys(d1).sort().reduce((obj, key) => {
        obj[key] = d1[key];
        return obj
    }, {});
    var newD2 = Object.keys(d2).sort().reduce((obj, key) => {
        obj[key] = d2[key];
        return obj
    }, {})
    newD1 = JSON.stringify(newD1)
    newD2 = JSON.stringify(newD2)
    
    return newD1 == newD2
};





var isAnagram = function(s, t) {
    var ss = s.length;
    var tt = t.length;
    if (ss != tt) {
        return false
    };
    d = {};
    for (var i = 0; i < ss; i++) {
        if (s[i] in d) {
            d[s[i]]++;
        }
        else {
            d[s[i]] = 1;
        }
    };
    for (var i = 0; i < tt; i++) {
        if (t[i] in d) {
            d[t[i]]--;
        }
        else {
            return false;
        }
    };
    for (let key in d) {
        if (d[key] !== 0) {
            return false
        }
    };
    return true;
    
};

/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */