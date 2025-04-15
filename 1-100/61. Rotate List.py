# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        leng = 1
        while curr.next:
            leng += 1
            curr = curr.next

        k %= leng
        if k == 0:
            return head

        curr.next = head
        new_tail = head
        for _ in range(leng - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        return new_head

