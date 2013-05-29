# encoding: utf-8

import sys
import os
testpath = os.path.dirname(os.path.realpath(__file__)) + "/test"
if not testpath in sys.path:
    sys.path.append(testpath)
from TestStuf import TestStuf


class MergeSorting(TestStuf):
    '''
    Conceptually, a merge sort works as follows
    Divide the unsorted list into n sublists,
each containing 1 element (a list of 1 element is considered sorted).
    Repeatedly merge sublists to produce new sublists
until there is only 1 sublist remaining. This will be the sorted list.
    '''

    def v1(self):
        '''top down'''
        def merge(l, r):
            L = []
            while len(l) > 0 or len(r) > 0:
                if len(l) > 0 and len(r) > 0:
                    if l[0] <= r[0]:
                        L.append(l[0])
                        l = l[1:]
                    else:
                        L.append(r[0])
                        r = r[1:]
                elif len(l) > 0:
                    L.append(l[0])
                    l = l[1:]
                else:
                    L.append(r[0])
                    r = r[1:]
            return L

        def msort(L):
            if len(L) <= 1:
                return L
            mid = len(L) / 2
            l = msort(L[0:mid])
            r = msort(L[mid:])
            return merge(l, r)

        self.L = msort(self.L)

    def v2(self):
        '''buttom up'''

sort = MergeSorting()
sort.run()
