// const mergeTwoLists = (list1, list2) => {
//     for(let i = 0; i < list2.length; i++) {
//         list1.push(list2[i])
//     }
//     // console.log(list1)
//     list1.sort()
//     return list1
// }

var mergeTwoLists = function(list1, list2) {
    const dummy = new ListNode(-Infinity);
    let prev = dummy;
    
    while(list1 && list2) {
        if(list1.val <= list2.val) {
            prev.next = list1;
            prev = list1;
            list1 = list1.next;
        }
        else {
            prev.next = list2;
            prev = list2;
            list2 = list2.next;
        }
    }
    if (!list1) prev.next = list2;
    if (!list2) prev.next = list1;
    
    return dummy.next
};

list1 = [1,2,4] 
list2 = [1,3,4]
console.log(mergeTwoLists(list1, list2))