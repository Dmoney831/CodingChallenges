var isValid = function(s) {
    var stack = [];
    const table = { '(':')', '{':'}', '[':']' };

    for (let i = 0; i < s.length; i++) {
        let par = s[i];
        if (table[par]) {
            stack.push(par);
        }
        else {
            if (stack.length == 0) {
                return false;
            }
            
            let z = stack.pop();
            if (par !== table[z]) {
                return false;
            } 
        }
    } console.log(stack.length == 0);
};

s = "()[]{}"
// s = "()"
isValid(s)