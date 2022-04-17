var groupAnagrams = function(strs) {
    const g = {};
    for (let i = 0; i < strs.length; i++) {
      let ordered = strs[i].split('').sort().join('');
      // console.log(ordered)
      if (!(ordered in g)) {
        g[ordered] = [strs[i]]
        // console.log(g)
      }
      else {
        g[ordered].push(strs[i])
        // console.log(g)
      }
    };
    console.log(g)
    console.log(Object.values(g))
};

var strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)

/**
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

 */