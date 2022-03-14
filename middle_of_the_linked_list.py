# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        length = self.checkDepth(head, 0)
        if length > 1:
            sol = self.traverseToDepth(head, 0, int(length / 2) + 1)
        else:
            sol = self.traverseToDepth(head, 0, length)
        return sol

    def checkDepth(self, head, counter):
        counter += 1
        if head.next is None:
            return counter
        else:
            return self.checkDepth(head.next, counter)

    def traverseToDepth(self, head, counter, depth):
        counter += 1
        if head.next is None:
            return ListNode(head.val, None)
        if counter >= depth:
            return ListNode(head.val, self.traverseToDepth(head.next, counter, depth))
        return self.traverseToDepth(head.next, counter, depth)

def createLinkedList(counter, depth):
    if counter == depth:
        return None
    counter += 1
    return ListNode(counter, createLinkedList(counter, depth))

# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
head = createLinkedList(0,5)
# print(x)
sol = Solution()
# head = [1,2,3,4,5,6]
print(sol.middleNode(head))