#!/usr/bin/env python3
# Program: ll-rm-duplicates.py
# Description:
#     Removes sequential duplicates of nodes' data in a linked-list DS.
# Date: 2021-10-03

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        if head is None: return
        current = head
        while current.next:
            try:
                while (current.data == current.next.data):
                    current.next = current.next.next
            except AttributeError:
                return head
            current = current.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);


