#

import sys
import os
testpath = os.path.dirname(os.path.realpath(__file__)) + "/test"
if not testpath in sys.path:
    sys.path.append(testpath)
from TestStuf import TestStuf


class InsertSorting(TestStuf):
    def v1(self):
        '''need extra space
        '''
        def insert(L, v):
            idx = 0
            while idx < len(L):
                if v < L[idx]:
                    L.insert(idx, v)
                    return
                idx = idx + 1
            L.append(v)
        L0 = self.L
        L1 = []
        for i in L0:
            insert(L1, i)
        self.L = L1

    def v2(self):
        L = self.L
        for i in range(1, len(L)):
            j = i - 1
            k = L[i]
            while L[j] > k and j >= 0:
                L[j + 1] = L[j]
                j -= 1
            L[j + 1] = k
        self.L = L

pop = InsertSorting()
pop.run()
