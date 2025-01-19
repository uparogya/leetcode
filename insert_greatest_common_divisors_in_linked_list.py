# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: list[ListNode]) -> list[ListNode]:

        def gcd(val1, val2):
            if val2 == 0:
                return val1
            else:
                return gcd(val2, val1%val2)

        first_li = head
        second_li = head.next

        while second_li:
            test_sum = ListNode(gcd(first_li.val,second_li.val))

            first_li.next = test_sum
            test_sum.next = second_li

            first_li = second_li
            second_li = second_li.next
        
        return head