# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        length = self.checkDepth(head, 0)
        newList = self.removeNode2(head, 0, length - n + 1, length)
        return newList

    def checkDepth(self, head, counter):
        counter +=1
        if head.next is None:
            return counter
        return self.checkDepth(head.next, counter)

    def removeNode(self, head, counter, limit):
        counter += 1
        # print(counter)
        if counter + 1 == limit:
            if head.next.next is None:
                return ListNode(head.val, None)
            else:
                return ListNode(head.val, self.removeNode(head.next.next, counter, limit))
        elif head.next is None:
            if counter == 1:
                return None
            else:
                return ListNode(head.val, None)
        elif limit == 1:
            return self.removeNode(head.next, counter, limit)
        else:
            return ListNode(head.val, self.removeNode(head.next, counter, limit))

    def removeNode2(self, head, counter, limit, length):
        counter += 1
        if limit == 1:
            if length == 1:
                return None
            elif head.next is None:
                return ListNode(head.val, None)
            elif counter == 1:
                if head.next.next is None:
                    return ListNode(head.next.val, None)
                else:
                    return ListNode(head.next.val, self.removeNode2(head.next.next, counter, limit, length))
            else:
                return ListNode(head.val, self.removeNode2(head.next, counter, limit, length))

        # print(counter)
        if counter + 1 == limit:
            if head.next.next is None:
                return ListNode(head.val, None)
            else:
                return ListNode(head.val, self.removeNode2(head.next.next, counter, limit, length))
        elif head.next is None:
            return ListNode(head.val, None)
        else:
            return ListNode(head.val, self.removeNode2(head.next, counter, limit, length))

def createLinkedList(counter, depth):
    if counter == depth:
        return None
    counter += 1
    return ListNode(counter, createLinkedList(counter, depth))

head = createLinkedList(0,5)
# print(x)
sol = Solution()
# head = [1,2,3,4,5,6]
print(sol.removeNthFromEnd(head, 2))