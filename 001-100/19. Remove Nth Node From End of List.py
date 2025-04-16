# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fake = ListNode(0, head)
        first = fake

        leng = 1
        curr = head
        while curr.next:
            leng += 1
            curr = curr.next

        for _ in range(leng - n):
            first = first.next
        first.next = first.next.next

        return fake.next