# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        i = head
        j = head
        while j and j.next:
            i = i.next
            j = j.next.next
        
        curr1 = i.next
        curr2 = None
        i.next = None
        while curr1:
            temp = curr1.next
            curr1.next = curr2
            curr2 = curr1
            curr1 = temp
        curr1 = head
        j = curr2
        while j:
            temp = curr1.next
            i = j.next
            curr1.next = j
            j.next = temp
            curr1 = temp
            j = i
        