#!/usr/bin/env python3
# Using list methods to replace user-defined queue class
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
        # declare and initialize <list> with 0th idx as <obj>Node
        queue = [root] if root else []

        # While list is not empty
        while queue:
            # Assign and remove next item in list
            current = queue.pop()
            print(current.data, end=" ")

            # Enqueue the current node's children
            if current.left: queue.insert(0,current.left)
            if current.right: queue.insert(0,current.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

