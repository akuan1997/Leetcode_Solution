# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        fake = ListNode(0, head)
        first = fake

        for _ in range(left - 1):
            first = first.next

        start = first.next
        curr = start

        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first.next = prev
        start.next = curr

        return fake.next
