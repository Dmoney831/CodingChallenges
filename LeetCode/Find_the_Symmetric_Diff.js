function sym() {
    var args = [];
    for (var i = 0; i < arguments.length; i++) {
      args.push(arguments[i]);
    }
  
    function symDiff(arrayOne, arrayTwo) {
      var result = [];
  
      arrayOne.forEach(function(item) {
        if (arrayTwo.indexOf(item) < 0 && result.indexOf(item) < 0) {
          result.push(item);
        }
      });
  
      arrayTwo.forEach(function(item) {
        if (arrayOne.indexOf(item) < 0 && result.indexOf(item) < 0) {
          result.push(item);
        }
      });
  
      return result;
    }
  
    // Apply reduce method to args array, using the symDiff function
    return args.reduce(symDiff);
  }
  console.log(sym([1, 2, 3], [5, 2, 1, 4]));



var sym = function(...args) {
    console.log(args)

    // const union = Array.from(new Set([...args[0], ...args[1]]))
    // console.log(union)

    // const intersection = args[0].filter(i => args[1].includes(i))
    // console.log(intersection)

    // const complement = args[0].filter(item => {return args[1].includes(item) === false})
    // console.log(complement)

    // const different = union.filter(item => {return intersection.includes(item) === false})
    // console.log(different)

    for (let i = 1; i < args.length; i++) {
        // firstTwo = [...args[i-1], ...args[i]]
        var intersection = args[i-1].filter(x => args[i].includes(x))
        var union = Array.from(new Set([...args[i-1], ...args[i]]))
        var different = union.filter(item => {return intersection.includes(item) === false})
        console.log(different)
        args[i] = different
    }
    return different
};

// sym([1, 2, 3], [5, 2, 1, 4]); // [3,4,5]
// sym([1, 2, 5], [2, 3, 5], [3, 4, 5]); // [1,3,4]
console.log(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])) // [1,4,5]