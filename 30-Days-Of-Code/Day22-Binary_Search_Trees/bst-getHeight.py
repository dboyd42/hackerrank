#!/usr/bin/env python3
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

    def getHeight(self,root):

        # Check if the binary tree is empty
        if root is None:
            return -1
        # Recursively call height of each node
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        # Return max(leftHeight, rightHeight) at each iteration and increment by 1
        return max(leftHeight, rightHeight) +1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)

