#!/usr/bin/env python3
# This code used a linked-list without a tail.
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # This should be 'add'
    def insert(self,head,data):
    #Complete this method
        current = self.head
        newNode = Node(data)
        if self.isEmpty():
            self.head = Node(data)
        else:
            # Traverse the linked-list
            while (current.next != None):
                current = current.next
            # Insert new node at tail
            current.next = newNode
        return self.head


