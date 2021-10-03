#!/usr/bin/env python3
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        if root is None: return
        q = Queue(root)
        # While there is >=1 discovered node
        while not q.isEmpty():
            curr = q.dequeue()
            print(curr.data, end=' ')
            if (curr.left is not None): q.enqueue(curr.left)
            if (curr.right is not None): q.enqueue(curr.right)

# Wrote a queue class to map discovered nodes
class Queue:
    def __init__(self, item):
        self.item = [item]
    def isEmpty(self):
        return self.item == []
    def enqueue(self, item):
        self.item.insert(0, item)
    def dequeue(self):
        return self.item.pop()
    def size(self):
        return len(self.item)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

