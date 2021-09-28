#!/usr/bin/env python3

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def __init__(self):
        self.head = None
        self.tail = self.head

    def isEmpty(self):
        return self.head == None

    def insert(self,head,data):
    #Complete this method
        tmp = Node(data)
        if (self.head is None):
            self.head = tmp
        elif (self.head == self.tail):
            self.head.next = tmp
        else:
            self.tail.next = tmp
        self.tail = tmp
        return self.head



mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
