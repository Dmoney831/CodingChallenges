var reverseList = function(head) {
    let prev = null, next = null, current = head;

    while(current !== null) {
        next = current.next
        current.next = prev
        prev = current 
        current = next
    }
    return prev
}