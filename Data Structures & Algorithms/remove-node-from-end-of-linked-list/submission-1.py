# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## Native Approach
        '''
        if head is None:
            return head
        
        k = 0

        curr = head

        while curr is not None:
            curr = curr.next
            k += 1

        
        if n > k:
            return head
        
        if k - n == 0:
            head = head.next
            return head
        
        curr = head

        for i in range(1, k - n):
            curr = curr.next

        
        curr.next = curr.next.next

        return head
        '''

        # Two pointer Approach

        dummy = ListNode(0)

        dummy.next = head

        slow = dummy
        fast = dummy

        for i in range(n + 1):
            if fast is None:
                return head
            
            fast = fast.next
        
        while fast is not None:
            fast = fast.next
            slow = slow.next

        nodeDeleted = slow.next

        if nodeDeleted is not None:
            slow.next = nodeDeleted.next
        
        return dummy.next


