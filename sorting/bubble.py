import sys
import os
testpath = os.path.dirname(os.path.realpath(__file__)) + "/test"
if not testpath in sys.path:
    sys.path.append(testpath)
from TestStuf import TestStuf


class BubbleSorting(TestStuf):
    def v1(self):
        '''dup loop for whole list, a most simple algorithm

        '''
        L = self.L
        size = self.size
        for i in range(size):
            for j in range(size - 1):
                if L[j] > L[j + 1]:
                    L[j], L[j + 1] = L[j + 1], L[j]
        self.L = L

    def v2(self):
        '''reduce the loop size,
        after each loop outside the end element should be the largest
        '''
        L = self.L
        for j in range(len(L) - 1, 1, -1):
            for i in range(0, j):
                if L[i] > L[i + 1]:
                    L[i], L[i + 1] = L[i + 1], L[i]
        self.L = L

bubble = BubbleSorting()
bubble.run()
