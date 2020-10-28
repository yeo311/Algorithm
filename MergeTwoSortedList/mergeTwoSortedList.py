# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example 1:

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: l1 = [], l2 = []
# Output: []

# Example 3:

# Input: l1 = [], l2 = [0]
# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultNode = None
        head = None
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                if resultNode == None:
                    resultNode = ListNode(l1.val)
                    head = resultNode
                else:
                    resultNode.next = ListNode(l1.val)
                    resultNode = resultNode.next
                l1 = l1.next
            else:
                if resultNode == None:
                    resultNode = ListNode(l2.val)
                    head = resultNode
                else:
                    resultNode.next = ListNode(l2.val)
                    resultNode = resultNode.next
                l2 = l2.next

        if l1 is not None:
            while l1 is not None:
                if resultNode == None:
                    resultNode = ListNode(l1.val)
                    head = resultNode
                else:
                    resultNode.next = ListNode(l1.val)
                    resultNode = resultNode.next
                l1 = l1.next
        elif l2 is not None:
            while l2 is not None:
                if resultNode == None:
                    resultNode = ListNode(l2.val)
                    head = resultNode
                else:
                    resultNode.next = ListNode(l2.val)
                    resultNode = resultNode.next
                l2 = l2.next
        return head
