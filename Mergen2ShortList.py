# Định nghĩa node của Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Tạo một node giả (dummy) để dễ thao tác
        dummy = ListNode()
        tail = dummy  # con trỏ hiện tại

        # So sánh từng node của 2 list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # di chuyển tail

        # Nếu 1 trong 2 list còn dư thì nối thẳng vào
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # Trả về head thật sự (bỏ qua node giả)
        return dummy.next
