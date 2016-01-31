/*
 * You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 *
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 *
 */
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
function ListNode(val) {
    this.val = val;
    this.next = null;
}

var addTwoNumbers = function(l1, l2){
    var sum = l1.val+l2.val;
    var next1 = l1.next;
    var next2 = l2.next;

    var l3 = new ListNode(sum%10);
    var node = l3;

    var carry_digit = Math.floor(sum/10);

    while(next1 || next2 || carry_digit) {
        var next_sum = (next1?next1.val:0)+(next2?next2.val:0)+carry_digit;
        node.next = new ListNode(next_sum%10);
        node = node.next;

        next1 = next1?next1.next:null;
        next2 = next2?next2.next:null;
        carry_digit = Math.floor(next_sum/10);

    }

    return l3;

};

var l1 = new ListNode(2);
l1.next = new ListNode(4);
l1.next.next = new ListNode(3);

var l2 = new ListNode(5);
l2.next = new ListNode(6);
l2.next.next = new ListNode(4);

print(addTwoNumbers(l1, l2));
