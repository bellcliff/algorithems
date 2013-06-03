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
        '''buttom up '''
        def merge(A, iL, iR, iEnd, B):
            #print 'L:%d,R:%d,E:%d' % (iL, iR, iEnd)
            i0 = iL
            i1 = iR
            for j in range(iL, iEnd):
                # If left list head exists and is <= existing right list head
                #print 'i0:%d, i1:%d' % (A[i0], A[i1])
                if i0 < iR and (i1 >= iEnd or A[i0] <= A[i1]):
                    B[j] = A[i0]
                    i0 += 1
                else:
                    B[j] = A[i1]
                    i1 += 1

        def bsort(L):
            B = list(L)
            width = 1
            n = len(L)
            while width < n:
                i = 0
                while i < n:
                    merge(L, i, min(i + width, n), min(i + 2 * width, n), B)
                    i += 2 * width
                width = 2 * width
                # Now work array B is full of runs of length 2*width
                for j in range(n):
                    L[j] = B[j]
                # Now array A is full of runs of length 2*width
            return L

        self.L = list(bsort(self.L))

sort = MergeSorting()
sort.run()
