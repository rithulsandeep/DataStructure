from collections import deque
import heapq
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def traverse_backward(self):
        curr = self.tail
        while curr:
            print(curr.data, end=' ')
            curr = curr.prev
        print()

#To show an example

dll = DoublyLinkedList()
dll.insert_head(1)
dll.insert_tail(2)
dll.insert_tail(3)
dll.traverse_forward()  # 1 2 3
dll.traverse_backward()  # 3 2 1ṇ