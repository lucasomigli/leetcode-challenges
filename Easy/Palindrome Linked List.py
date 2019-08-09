# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        return stack == [stack[i] for i in range(len(stack)-1, -1, -1)]
