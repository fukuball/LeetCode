"""
 * q1-add-two-numbers.py
 *
 * @param {ListNode} l1
 * @param {ListNode} l2
 *
 * @return {ListNode}
"""
import math


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        add_two_sum = l1.val + l2.val
        next1 = l1.next
        next2 = l2.next

        l3 = ListNode(add_two_sum % 10)
        node = l3

        carry_digit = int(math.floor(add_two_sum/10))

        while (next1 or next2 or carry_digit):
            next_sum = (next1.val if next1 else 0) + (next2.val if next2 else 0) + carry_digit
            node.next = ListNode(next_sum % 10)
            node = node.next

            next1 = next1.next if next1 else None
            next2 = next2.next if next2 else None
            carry_digit = int(math.floor(next_sum / 10))

        return l3

##------------------------------ Simple Testing Code ------------------------------##

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)
print(l3.val)
print(l3.next.val)
print(l3.next.next.val)
