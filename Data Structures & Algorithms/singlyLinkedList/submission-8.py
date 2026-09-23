class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(float('inf'))  # Dummy node
        self.tail = self.head

    def get(self, index: int) -> int:
        temp = self.head.next  # Start at the first actual node
        while index and temp:
            temp = temp.next
            index -= 1
        return temp.val if temp else -1  # Return -1 if index is invalid

    def insertHead(self, val: int) -> None:
        temp = self.head.next
        self.head.next = ListNode(val, temp)
        if self.tail == self.head:  # Update tail if the list was empty
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        temp = self.head
        while index and temp.next:  # Ensure `temp.next` exists
            temp = temp.next
            index -= 1
        if temp.next:  # Node to remove exists
            if temp.next == self.tail:  # Update tail if last node is removed
                self.tail = temp
            temp.next = temp.next.next
            return True
        return False

    def getValues(self) -> list[int]:
        temp = self.head.next
        values = []
        while temp:
            values.append(temp.val)
            temp = temp.next
        return values

