# 두 개의 숫자 리스트를 각 자리수를 가진 하나의 수로 생각하고 덧셈하는 문제
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overNum = 0
        result = None
        head = None
        while l1 or l2:
            if l1 and l2:
                tmp = l1.val + l2.val
                if overNum != 0:
                    tmp += overNum
                    overNum = 0

                if tmp >= 10:
                    overNum = 1
                    tmp -= 10
                if result == None:
                    result = ListNode(tmp)
                    head = result
                else:
                    result.next = ListNode(tmp)
                    result = result.next
                l1 = l1.next
                l2 = l2.next
            else:
                tmp = 0
                if overNum != 0:
                    tmp = overNum
                    overNum = 0
                if l1:
                    tmp += l1.val
                    if tmp >= 10:
                        overNum = 1
                        tmp -= 10
                    if result == None:
                        result = ListNode(tmp)
                        head = result
                    else:
                        result.next = ListNode(tmp)
                        result = result.next
                    l1 = l1.next
                elif l2:
                    tmp += l2.val
                    if tmp >= 10:
                        overNum = 1
                        tmp -= 10
                    if result == None:
                        result = ListNode(tmp)
                        head = result
                    else:
                        result.next = ListNode(tmp)
                        result = result.next
                    l2 = l2.next
        if overNum != 0:
            result.next = ListNode(overNum)

        return head
