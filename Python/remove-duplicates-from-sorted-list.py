from __future__ import print_function
# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            runner = cur.next
            while runner and runner.val == cur.val:
                runner = runner.next
            cur.next = runner
            cur = runner
        return head

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        if head.next:
            if head.val == head.next.val:
                head = self.deleteDuplicates(head.next)
            else:
                head.next = self.deleteDuplicates(head.next)
        return head


if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    print(Solution().deleteDuplicates(head))

