# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        leng = 1
        while curr.next:
            leng += 1
            curr = curr.next

        fake = ListNode(0, head)
        prev_group = fake

        for _ in range(leng // k):
            curr = prev_group.next

            prev = None
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            next_group = prev_group.next
            prev_group.next = prev
            next_group.next = curr
            prev_group = next_group

        return fake.next