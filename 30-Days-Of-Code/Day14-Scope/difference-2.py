#!/usr/bin/env python3

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        for i in range(len(self.__elements)-1):
            for j in range(len(self.__elements)-1):
                diff = abs(self.__elements[i] - self.__elements[j+1])
                if (diff > self.maximumDifference):
                    self.maximumDifference = diff
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)

