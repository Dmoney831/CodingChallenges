var MinStack = function() {
    this.min = [];
    this.stack = [];
};

MinStack.prototype.push = function(val) {
    this.stack.push(val)
    if (this.min.length === 0 || x <= this.min[this.min.length - 1]) 
    this.min.push(x);
    this.stack.push(x);
};

MinStack.prototype.pop = function() {
    var val = this.stack.pop();
    if (val === this.min[this.min.length - 1]) this.min.pop();
};

MinStack.prototype.top = function() {
    return this.stack.length ? this.stack[this.stack.length - 1] : 0;
};

MinStack.prototype.getMin = function() {
    return this.min.length ? this.min[this.min.length -1] : 0;
};