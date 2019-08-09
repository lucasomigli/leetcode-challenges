class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False
        fast, slow = (head, head)
        while fast != None and slow != None:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                return False

            if slow == fast:
                return True

        return False
