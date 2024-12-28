class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = self.head.next
            current_node.next = None
        if self.head is None:
            self.tail = None
