class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while True:
            if head == None:
                return
            elif head.val == val:
                head = head.next
            else:
                break

        p: ListNode = head

        while p.next != None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head
