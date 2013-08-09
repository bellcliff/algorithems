import sys
import os
testpath = os.path.dirname(os.path.realpath(__file__)) + "/test"
if not testpath in sys.path:
    sys.path.append(testpath)
from TestStuf import TestStuf


class HeapSorting(TestStuf):
    def v1(self):
        '''
        '''

        def heapify(a, count):
            '''
            create heap as a max-heap
            '''
            start = count / 2 - 1
            while start >= 0:
                sift(a, start, count - 1)
                start = start - 1

        def sift(a, start, end):
            root = start
            while root * 2 + 1 <= end:
                child = root * 2 + 1
                swap = root
                if a[swap] < a[child]:
                    swap = child
                if child + 1 <= end and a[swap] < a[child + 1]:
                    swap = child + 1
                if swap != root:
                    a[root], a[swap] = a[swap], a[root]
                    root = swap
                else:
                    return

        L = self.L
        count = len(L)
        heapify(L, count)
        end = count - 1
        while end > 0:
            # swap heap root as last element
            L[end], L[0] = L[0], L[end]
            # duplicate the heapify and sift
            end -= 1
            sift(L, 0, end)
            
    def v2(self):
        ''''''
        def LEFT(i):
            return 2 * i + 1
        def RIGHT(i):
            return 2 * i + 2
        def PARENT(i):
            return i / 2
        def max_heap(A, i):
            '''max-heap'''
            l = LEFT(i)
            r = RIGHT(i)            
            if l < len(A) and A[l] > A[i]:
                largest = l
            else: largest = i
            if r < len(A) and A[r] > A[largest]:
                largest = r
            if largest != i:
                A[i], A[largest] = A[largest], A[i]
                max_heap(A, largest)
                
        def build_max_heap(A):
            start = len(A)/2
            while start>0:
                max_heap(A, start)
                
        L = self.L
        count = len(L)
        end = count
        while end > 0:
            max_heap(L, 0, end)            
            L[end-1], L[0] = L[0], L[end-1]
            end = end-1


heap = HeapSorting()
heap.run()
