// var romanToInt = function(s) {
//     var dict = { "I":1, "V":5,  "X":10, "L":50, "C":100, "D":500, "M":1000};
//     let output = 0;
//     for (let i in "III") {
        
//         console.log(i)
//         console.log(dict[i])
//         console.log(1000)
//     };
//     console.log(output)
    
// };

var romanToInt = function(s) {
    var dict = { "I":1, "V":5,  "X":10, "L":50, "C":100, "D":500, "M":1000};
    
    let output = 0
    for (let i = 0; i < s.length; i++) {
        if (dict[s[i]] < dict[s[i+1]]) {
            output -= dict[s[i]]
        }
        else {
            output += dict[s[i]]
        }
    }
    console.log(output)
    return output
}

s = "MCMXCIV"
// s = "III"
romanToInt(s)