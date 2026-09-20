"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Using Hash Map
        '''
        nodeMap = {}
        curr = head

        while curr is not None:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr is not None:
            newNode = nodeMap[curr]
            newNode.next = nodeMap.get(curr.next)

            newNode.random = nodeMap.get(curr.random)
            curr = curr.next

        
        return nodeMap.get(head)

        '''
        # Optimized approach O(n) time and O(1) space

        if head is None:
            return None

        curr = head

        while curr is not None:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next
        
        curr = head
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            
            curr = curr.next.next
        

        curr = head
        clonedHead = head.next
        clone = clonedHead
        
        while clone.next is not None:
            curr.next = curr.next.next
            clone.next = clone.next.next

            curr = curr.next
            clone = clone.next
        
        curr.next = None
        clone.next = None


        return clonedHead

