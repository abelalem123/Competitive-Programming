class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = None
        self.last = None
        self.size = k

    def insertFront(self, value: int) -> bool:
        if not self.size: return False
        new_node = Node(value)
        if not self.head: 
            self.head = new_node
            self.last = self.head
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size -= 1
        return True

    def insertLast(self, value: int) -> bool:
        if not self.size: return False
        new_node = Node(value)
        if not self.head: 
            self.head = new_node
            self.last = self.head
        else: 
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
        self.size -= 1
        return True

    def deleteFront(self) -> bool:
        if not self.head: return False
        if not self.head.next: 
            self.head = None
            self.last = None
        else: 
            next_node = self.head.next
            self.head.next = None
            next_node.prev = None
            self.head = next_node
        self.size += 1
        return True

    def deleteLast(self) -> bool:
        if not self.head: return False
        if not self.head.next:
            self.head = None
            self.last = None
        else:
            prev_node = self.last.prev
            self.last.next = None
            self.last.prev = None
            prev_node.next = None
            self.last = prev_node
        self.size += 1
        return True

    def getFront(self) -> int:
        if self.head: return self.head.val
        return -1

    def getRear(self) -> int:
        if self.last: return self.last.val
        return -1

    def isEmpty(self) -> bool:
        return True if not self.head else False

    def isFull(self) -> bool:
        return True if not self.size else False