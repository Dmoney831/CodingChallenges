var generateParenthesis = function(n) {
    var res = []
    
    if (n < 1) return res;
    var generate = function (res, str, ll, rr) {
        if (ll || rr) {
            if (rr > ll) generate(res, str + ')', ll, rr - 1)
            if (ll) generate(res, str + '(', ll - 1, rr);
        } else {
            res.push(str)
        }
    }
    generate(res, '', n, n);
    return res;
};


// Time Complexity : O( (4^n)/(n^(-1)) )?
// Space Complexity: O( (4^n)/(n^(-1)) )?