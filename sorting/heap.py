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


heap = HeapSorting()
heap.run()
