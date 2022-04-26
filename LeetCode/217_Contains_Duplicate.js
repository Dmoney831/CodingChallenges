var containsDuplicate = function(nums) {
    var x = [...new Set(nums)];
    return x.length != nums.length
    
  };
  
var nums = [1,2,3,1]
containsDuplicate(nums)