# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(l1, l2):
            fake = ListNode(0)
            curr = fake

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return fake.next

        def merge(lists, left, right):
            if left == right:
                return lists[left]
            if left > right:
                return None

            mid = (left + right) // 2
            l1 = merge(lists, left, mid)
            l2 = merge(lists, mid + 1, right)
            return mergeTwoLists(l1, l2)

        return merge(lists, 0, len(lists) - 1)
