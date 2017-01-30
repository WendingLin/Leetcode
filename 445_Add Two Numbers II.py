#445.Add Two Numbers II
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1, stack2=[], []
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next
        value=0
        carry=0
        header=ListNode(0) #header.next=None
        while len(stack1)>0 or len(stack2)>0 or carry:
            value=0
            if len(stack1)>0:
                value+=stack1.pop()
            if len(stack2)>0:
                value+=stack2.pop()
            value+=carry
            carry=int(value/10)
            value=value%10
            node=ListNode(value)
            node.next=header.next
            header.next=node
        return header.next