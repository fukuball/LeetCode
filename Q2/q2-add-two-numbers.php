<?php
/*
 * You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 *
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 *
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
class ListNode {

    public $val;
    public $next;

    function __construct($val) {
        $this->val = $val;
        $this->next = null;
    }
}

function addTwoNumbers($l1, $l2) {
    $sum = $l1->val+$l2->val;
    $next1 = $l1->next;
    $next2 = $l2->next;

    $l3 = new ListNode($sum%10);
    $node = $l3;

    $carray_digit = floor($sum/10);

    while($next1 || $next2 || $carry_digit) {

        $next1_v = $next1!==null?$next1->val:0;
        $next2_v = $next2!==null?$next2->val:0;

        $next_sum = $next1_v+$next2_v+$carry_digit;
        $node->next = new ListNode($next_sum%10);
        $node = $node->next;

        $next1 = $next1!==null?$next1->next:null;
        $next2 = $next2!==null?$next2->next:null;
        $carry_digit = floor($next_sum/10);
    }

    return $l3;

}


$l1 = new ListNode(2);
$l1->next = new ListNode(4);
$l1->next->next = new ListNode(3);

$l2 = new ListNode(5);
$l2->next = new ListNode(6);
$l2->next->next = new ListNode(4);

var_dump(addTwoNumbers($l1, $l2));